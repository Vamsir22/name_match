import pandas as pd

input_names = pd.read_excel('Strategy.xlsx')

try:
    prod_names = []
    sus_names = []
    for i in range(20001, len(input_names)):
        # cid = str(input_names.cid.iloc[i])
        first_name = str(input_names.first_name.iloc[i])
        second_name = str(input_names.second_name.iloc[i])
        # matched_rule = str(input_names.matched_rule.iloc[i])

        if not all(x.isalpha() or x.isspace() for x in first_name):
            sus_names.append(first_name)
        if not all(x.isalpha() or x.isspace() for x in second_name):
            sus_names.append(second_name)

        # first_name_split = first_name.split(" ")
        # second_name_split = second_name.split(" ")
        #
        # a = min(len(each) for each in first_name_split)
        # b = min(len(each) for each in second_name_split)
        #
        # # print(a, b)
        #
        # if a == b == 1:
        #     print(first_name,",", second_name)

        # if matched_rule == 'R002':
        #     names = (first_name, second_name)
        #     prod_names.append(names)

    print(sus_names)

except Exception as e:
    print("error occured: ", e)

