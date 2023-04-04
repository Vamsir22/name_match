import pandas as pd

input_names = pd.read_excel('Strategy.xlsx')

try:
    mismatched_list = []
    matched_rule_dict = {}
    # mismatched_list_new_low = []
    for i in range(0, 10000):
        existing_score = int(input_names.existing_score.iloc[i])
        name_score = int(input_names.name_score.iloc[i])
        cid = str(input_names.cid.iloc[i])
        matched_rule = str(input_names.matched_rule.iloc[i])

        if existing_score <= 100 and existing_score != -9999 and existing_score != name_score:
            matched_rule_dict[matched_rule] = matched_rule_dict.get(matched_rule, 0) + 1
            # mismatched_list.append(cid)
            # if existing_score > name_score:
            #     mismatched_list_new_low.append(cid)

    print(matched_rule_dict)


    # print('mismatched_list',mismatched_list)
    # print("mismatched_list_new_low", mismatched_list_new_low)

    # matched_rule = []

    # mismatched_list_new_low = ['25109314', '14919302', '8935706']
    # cid_list = []
    # for each in mismatched_list_new_low:
    #     # print(each)
    #     a = input_names.loc[input_names['cid'] == int(each), 'matched_rule']
    #     matched_rule.append(a.iloc[0])
    #     if a.iloc[0] == 'R003':
    #         cid_list.append(each)
    #     # print(a)
    # # print(matched_rule)
    # print(cid_list)
except Exception as e:
    print("error occured: ", e)

