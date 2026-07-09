from sklearn.base import BaseEstimator, TransformerMixin


class FeatureStore(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.ma_dictionary = {}

    def fit(self, X, y=None):
        df = X.copy()
        df['duration'] = (df['time_to'] - df['time_from']).dt.total_seconds()

        # Create dict for duration 7 days moving average with 1 day shift calculation for worker - item - process - date combo
        daily_stats = df.assign(date=df['time_from'].dt.normalize())\
            .groupby(['worker_id', 'item_id', 'process_name', 'date'], as_index=False)['duration']\
            .mean()
        daily_stats['ma_duration'] = daily_stats.sort_values('date')\
            .groupby(['worker_id', 'item_id', 'process_name'])['duration']\
            .transform(lambda s: s.shift(1).rolling(7, min_periods=1).mean())
        self.ma_dict = daily_stats.set_index(['worker_id', 'item_id', 'process_name', 'date'])['ma_duration'].to_dict()
        
        return self

    def transform(self, X):
        df = X.copy()
        
        # Create features from date
        df['weekday'] = df['time_from'].dt.weekday
        df['day'] = df['time_from'].dt.day
        df['date'] = df['time_from'].dt.normalize()
        
        # Map MA duration by worker - item - process - date combo
        df['ma_duration'] = df.apply(
            lambda row: self.ma_dict.get((row['worker_id'], row['item_id'], row['process_name'], row['date'])),
            axis=1
        )
        
        # Return only features
        categorical_features = ['worker_id', 'item_id', 'process_name'] 
        numerical_features = ['weekday', 'day', 'ma_duration']
        X_out = df[categorical_features + numerical_features].copy()

        X_out['ma_duration'] = X_out['ma_duration'].astype(float)

        # Change categorical feature type to category to pass it to LightGBM
        for f in categorical_features:
            X_out[f] = X_out[f].astype('category')
        
        return X_out
        