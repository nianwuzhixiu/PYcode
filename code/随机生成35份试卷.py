# py3
# 随机生成试卷，有问题和答案

import random

# 测试数据，键是州，值是首都
capitals = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Indiana": "Indianapolis",
    "Iowa": "Des Moines",
    "Kansas": "Topeka",
    "Kentucky": "Frankfort",
    "Louisiana": "Baton Rouge",
    "Maine": "Augusta",
    "Maryland": "Annapolis",
    "Massachusetts": "Boston",
    "Michigan": "Lansing",
    "Minnesota": "Saint  Paul",
    "Mississippi": "Jackson",
    "Missouri": "Jefferson City",
    "Montana": "Helena",
    "Nebraska": "Lincoln",
    "Nevada": "Carson City",
    "New Hampshire": "Concord",
    "New Jersey": "Trenton",
    "NewMexico": "Santa Fe",
    "New York": "Albany",
    "North Carolina": "Raleigh",
    "North Dakota": "Bismarck",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Rhode Island": "Providence",
    "South Carolina": "Columbia",
    "South Dakota": "Pierre",
    "Tennessee": "Nashville",
    "Texas": "Austin",
    "Utah": "Salt Lake City",
    "Vermont": "Montpelier",
    "Virginia": "Richmond",
    "Washington": "Olympia",
    "West Virginia": "Charleston",
    "Wisconsin": "Madison",
    "Wyoming": "Cheyenne",
}

Num=0
# 循环生成35份试卷以及答案文件
for sjnum in range(35):
    # 创建文件
    quizFile = open(f"capitalsquiz{sjnum+1}.docx", "w")
    answerKeyFile = open(f"answer_{sjnum+1}.docx", "w")
    # 编写试卷开头
    quizFile.write("姓名：\n\n班级：\n\n成绩：\n\n")
    quizFile.write((" " * 15) + "自由美利坚州省会测试")
    quizFile.write("\n\n")
    # 打乱州列表顺序
    states = list(capitals.keys())
    random.shuffle(states)
    # 遍历每个州，每个周当成一个问题
    for questionNum in range(50):
        correctAnswer = capitals[states[questionNum]]
        wrongAnswer = list(capitals.values())
        del wrongAnswer[wrongAnswer.index(correctAnswer)]
        wrongAnswer = random.sample(wrongAnswer, 3)
        answerOption = wrongAnswer + [correctAnswer]
        random.shuffle(answerOption)
        # 写入问题
        quizFile.write(f"{questionNum+1}.美利坚{states[questionNum]}的省会是哪个？\n")
        for i in range(4):
            quizFile.write(f"  {'ABCD'[i]}.{answerOption[i]}  ")
        quizFile.write("\n")
        # 把答案写入答案文件
        answerKeyFile.write(
            f"{questionNum+1}.{'ABCD'[answerOption.index(correctAnswer)]}  "
        )
    quizFile.close()
    answerKeyFile.close()
    Num+=2
print(f'生成了{Num}个文件')
