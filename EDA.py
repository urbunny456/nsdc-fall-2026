import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Names of files
# calc_case_description_test_set.csv
# calc_case_description_train_set.csv
# mass_case_description_test_set.csv
# mass_case_description_train_set.csv



#Plotting the Count of a specific data
def plot_count(file_name, data_name):
    df = pd.read_csv(file_name)
    data_col = df[data_name]
    data_cnt = data_col.value_counts()

    sns.barplot(y=data_cnt.index, x=data_cnt.values)

    plt.title(f"Count for {data_name}")
    plt.xlabel("Count")

    plt.tight_layout()
    plt.show()



#Plotting Breast Density and Pathology Relation
def plot_B_and_P(file_name):
    df = pd.read_csv(file_name)
    if file_name.startswith("calc"):
        series_B = df["breast density"]
    elif file_name.startswith("mass"):
        series_B = df["breast_density"]
    else:
        raise(ValueError("File name not considered"))

    series_B_val_count = series_B.value_counts()


    # print(series_B_val_count)

    series_P = df["pathology"]

    df_B_P = pd.DataFrame({"breast density": series_B, "pathology": series_P})

    # print(df_B_P)


    series_counts = df_B_P[["breast density", "pathology"]].value_counts()


    # print(series_counts)

    series_counts_df = series_counts.reset_index()

    print(series_counts_df)

    print(series_B_val_count)

    series_counts_df["percentage"] = (series_counts_df["count"] / series_counts_df["breast density"].map(series_B_val_count))
    print(series_counts_df)

    fig = plt.figure(figsize=(11,5))
    ax1 = fig.add_subplot(1,2,1)
    ax2 = fig.add_subplot(1,2,2)

    ax1 = sns.barplot(data=series_counts_df, x="breast density",y="count", hue="pathology", ax=ax1)
    ax1.set_title("Comparing Breast Density and Pathology")

    

    ax2 = sns.barplot(data=series_counts_df, x="breast density",y="percentage", hue="pathology", ax=ax2)
    ax2.set_title("Comparing Breast Density and Pathology Percentage")


    plt.tight_layout()
    plt.show()



#_____________________Plotting Unique Counts of Abnormality Type______________
#Calcification
# plot_count("calc_case_description_test_set.csv", "calc type")
# plot_count("calc_case_description_train_set.csv", "calc type")

#Mass Shape
# plot_count("mass_case_description_test_set.csv", "mass shape")
# plot_count("mass_case_description_train_set.csv", "mass shape")




#_____________________Plotting Breast Density and Pathology and Ratios of malignant or benign______________
#Calc Data Set
# plot_B_and_P("calc_case_description_test_set.csv")
# plot_B_and_P("calc_case_description_train_set.csv")

#Mass Data Set
# plot_B_and_P("mass_case_description_test_set.csv") 
# plot_B_and_P("mass_case_description_train_set.csv")
