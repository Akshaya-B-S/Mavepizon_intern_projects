<<<<<<< HEAD
import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

#to dump tha model into file import pickle
import pickle
df = pd.read_csv("C:/Users/acer/PycharmProjects/PythonProject1/datasets_downloads/shopping_trends.csv")

# print(df.info())
# print(df.isnull().sum())
# print(df.duplicated().sum())
df.columns = df.columns.str.strip()

top10 = df['Customer ID'].value_counts()
print(top10)

df = df.drop("Customer ID", axis=1)

print(df.columns.tolist())
x = df.drop('Category', axis =1)
y = df['Category']

x = pd.get_dummies(x)  #y using get_dummies here cause it affect category if u use it for full df, only for x
le = LabelEncoder()  #use it only for y
y = le.fit_transform(y)


x_train, x_test,y_train, y_test = train_test_split(x,y, test_size = 0.2, random_state = 43)

model = XGBClassifier( n_estimators=100,
    learning_rate=0.1,
    max_depth=6,random_state=42)

# print(y_test)
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
# print(y_pred)
print("accuracy:",accuracy_score(y_test, y_pred))

new_data = pd.DataFrame([[67,'Female','Coat',20,'Minnesota','M','Blue','Spring',3.9,'No','Debit Card','Next Day Air','No',
                          'No',39,'Credit Card','Fortnightly'
]],
                        columns =  ['Age', 'Gender', 'Item Purchased', 'Purchase Amount (USD)','Location', 'Size', 'Color', 'Season',
                    'Review Rating', 'Subscription Status', 'Payment Method',  'Shipping Type', 'Discount Applied', 'Promo Code Used',
                    'Previous Purchases', 'Preferred Payment Method', 'Frequency of Purchases'])

new_data = pd.get_dummies(new_data)
new_data = new_data.reindex(columns=x_train.columns, fill_value=0)  #rearranges them into the exact same order
ans = model.predict(new_data)
pred = le.inverse_transform(ans)[0]

print(pd.Series(pred).value_counts())

# pickle.dump(model, open('model.pkl','wb'))
# model1 = pickle.load(open('model.pkl','rb'))
#
# model1.predict(new_data)
# ans = model1.predict(new_data)
# pred = le.inverse_transform(ans)[0]
#
# print(pd.Series(pred).value_counts())

# Save everything
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("label_encoder.pkl", "wb") as f:
    pickle.dump(le, f)

with open("columns.pkl", "wb") as f:
    pickle.dump(x_train.columns.tolist(), f)

=======
import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

#to dump tha model into file import pickle
import pickle
df = pd.read_csv("C:/Users/acer/PycharmProjects/PythonProject1/datasets_downloads/shopping_trends.csv")

# print(df.info())
# print(df.isnull().sum())
# print(df.duplicated().sum())
df.columns = df.columns.str.strip()

top10 = df['Customer ID'].value_counts()
print(top10)

df = df.drop("Customer ID", axis=1)

print(df.columns.tolist())
x = df.drop('Category', axis =1)
y = df['Category']

x = pd.get_dummies(x)  #y using get_dummies here cause it affect category if u use it for full df, only for x
le = LabelEncoder()  #use it only for y
y = le.fit_transform(y)


x_train, x_test,y_train, y_test = train_test_split(x,y, test_size = 0.2, random_state = 43)

model = XGBClassifier( n_estimators=100,
    learning_rate=0.1,
    max_depth=6,random_state=42)

# print(y_test)
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
# print(y_pred)
print("accuracy:",accuracy_score(y_test, y_pred))

new_data = pd.DataFrame([[67,'Female','Coat',20,'Minnesota','M','Blue','Spring',3.9,'No','Debit Card','Next Day Air','No',
                          'No',39,'Credit Card','Fortnightly'
]],
                        columns =  ['Age', 'Gender', 'Item Purchased', 'Purchase Amount (USD)','Location', 'Size', 'Color', 'Season',
                    'Review Rating', 'Subscription Status', 'Payment Method',  'Shipping Type', 'Discount Applied', 'Promo Code Used',
                    'Previous Purchases', 'Preferred Payment Method', 'Frequency of Purchases'])

new_data = pd.get_dummies(new_data)
new_data = new_data.reindex(columns=x_train.columns, fill_value=0)  #rearranges them into the exact same order
ans = model.predict(new_data)
pred = le.inverse_transform(ans)[0]

print(pd.Series(pred).value_counts())

# pickle.dump(model, open('model.pkl','wb'))
# model1 = pickle.load(open('model.pkl','rb'))
#
# model1.predict(new_data)
# ans = model1.predict(new_data)
# pred = le.inverse_transform(ans)[0]
#
# print(pd.Series(pred).value_counts())

# Save everything
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("label_encoder.pkl", "wb") as f:
    pickle.dump(le, f)

with open("columns.pkl", "wb") as f:
    pickle.dump(x_train.columns.tolist(), f)

>>>>>>> 5c451a6 (Initial commit)
print("Model saved successfully!")