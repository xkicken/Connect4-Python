def convert_to_percent(scores_list, out_of):
    precent = 0
    for i in range(len(scores_list)):
        precent = float(scores_list[i]) *  (100 / out_of)
        print(float(scores_list[i]) *  (100 / out_of))
        scores_list[i] = precent

marks = [25.5, 50, 49, 15.9, 0]
convert_to_percent(marks, 50)
print("Marks out of 100:", marks)

