import numpy as np
import pandas as pd
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


##
def clean(df):
	df['LotFrontage'].fillna(round(df['LotFrontage'].mean()), inplace=True)
	df['MasVnrType'].fillna('None', inplace=True)
	df['MasVnrArea'].fillna(0, inplace=True)
	df['Electrical'].fillna(df['Electrical'].value_counts().index[0],
	                        inplace=True)
	df['GarageYrBlt'].where(np.isfinite(df['GarageYrBlt']),
	                        df['YearBuilt'], inplace=True)

	try:
		df.fillna('NA', inplace=True)
		target = df['SalePrice']
		df.drop('SalePrice', axis=1, inplace=True)

		return df, target
	except KeyError:
		cols = ['BsmtFinSF1', 'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF',
		        'BsmtFullBath', 'BsmtHalfBath', 'GarageCars', 'GarageArea']
		df[cols] = df[cols].replace('NA', np.nan)
		df[cols] = df[cols].apply(pd.to_numeric)
		df[cols] = df[cols].where(np.isfinite(df[cols]), round(df[cols].mean()),
		                          axis=1)
		return df


##
X_train, y_train = clean(pd.read_csv('dataset/train.csv'))
X_test = clean(pd.read_csv('dataset/test.csv'))

##

