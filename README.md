# kaggle_titanic_competition
https://www.kaggle.com/c/titanic/data?select=train.csv

## Data summary: 
Data summary
    'PassengerId'
        Id (891)
    
    'Survived'
        Classification variable
        2 values: 
            0 (549)
            1 (342)
    
    'Pclass'
        3 values: 
            1 (216)
            2 (184)
            3 (491)
    
    'Name'
        891 unique values
    
    'Sex'
        male (65%)
        female (35%)
    
    'Age'
        MISSING (177)
        Mean: 29.7
        Std. deviation: 14.5
        Min: 0.42
        Max: 80
        Double
    
    'SibSp'
        Number of siblings / spouses aboard the sheep
        Min: 0 (608)
        Max: 8 (7)
    
    'Parch'
        Number of parents / children aboard the sheep
        Min: 0 (678)
        Max: 6
    
    'Ticket'
        618 unique values
    
    'Fare'
        Double
    
    'Cabin'
        Cabin number
        MISSING (687 - 77%)
        \w{1}(\d{1,3))?((\s)\w{1}(\d{1,3)))*
        print(train_df.Cabin.loc[-train_df.Cabin.isnull()])
    
    'Embarked'
        MISSING (2)
        C = Cherbourg (19%)
        Q = Queenstown (9%)
        S = Southampton (72%)