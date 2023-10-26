import pdftotext
from pathlib import Path

units = {
    'Patterns': {'file': 'Patterns', 'year': 1, "order": 1, 'activities': {}},
    'The Overland Trail': {'file': 'The_Overland_Trail', 'year': 1, "order": 2, 'activities': {}},
    'The Pit and the Pendulum': {'file': 'The_Pit_and_the_Pendulum', 'year': 1, "order": 3, 'activities': {}},
    'Shadows': {'file': 'Shadows', 'year': 1, "order": 4, 'activities': {}},
    'Cookies': {'file': 'Cookies', 'year': 1, "order": 5, 'activities': {}},
    'All About Alice': {'file': 'All_About_Alice', 'year': 1, "order": 6, 'activities': {}},
    'Fireworks': {'file': 'Fireworks', 'year': 2, "order": 1, 'activities': {}},
    'Geometry by Design': {'file': 'Geometry_by_Design', 'year': 2, "order": 2, 'activities': {}},
    'Game of Pig': {'file': 'Game_of_Pig', 'year': 2, "order": 3, 'activities': {}},
    'Do Bees Build It Best?': {'file': 'Do_Bees_Build_It_Best', 'year': 2, "order": 4, 'activities': {}},
    "Small World Isn't It?": {'file': 'Small_World', 'year': 2, "order": 5, 'activities': {}},
    'Pennant Fever': {'file': 'Pennant_Fever', 'year': 3, "order": 1, 'activities': {}},
    'Orchard Hideout': {'file': 'Orchard_Hideout', 'year': 3, "order": 2, 'activities': {}},
    'High Dive': {'file': 'High_Dive', 'year': 3, "order": 3, 'activities': {}},
    'World of Functions': {'file': 'World_of_Functions', 'year': 3, "order": 4, 'activities': {}},
    'Is There Really a Difference?': {'file': 'Is_There_Really_a_Difference', 'year': 3, "order": 5, 'activities': {}},
    'Meadows or Malls?': {'file': 'Meadows_or_Malls', 'year': 4, "order": 1, 'activities': {}},
    "The Pollster's Dilemma": {'file': 'Pollsters_Dilemma', 'year': 4, "order": 2, 'activities': {}},
    'How Much? How Fast?': {'file': 'How_Much_How_Fast', 'year': 4, "order": 3, 'activities': {}},
    'As the Cube Turns': {'file': 'As_the_Cube_Turns', 'year': 4, "order": 4, 'activities': {}}
 }

ftg_path = Path.cwd() / 'Full Teacher Guides'
all_pdf_files = list(Path(ftg_path).glob('*.pdf'))

activity_count = 0
current_unit = None
for pdf_path in all_pdf_files:
    for u in units:
        if units[u]['file'] == pdf_path.stem:
            current_unit = u

    with open(pdf_path, 'rb') as f:
        pdf = pdftotext.PDF(f)

    all_pdf_text = "\n\n".join(pdf)

    start = all_pdf_text.find("Activity Notes")
    end = all_pdf_text.find("Blackline Masters", start)
    if current_unit == "Do Bees Build It Best?":
        end = all_pdf_text.find("Calculator Guide and Calculator Notes", start)
    activities_split = all_pdf_text[start: end].split('\n')
    first_activity_name = ""
    order_count = 0
    for raw_activity_name in activities_split:
        activity_name = raw_activity_name.strip()
        if activity_name == "Put You Fist Into It":
            activity_name = "Put Your Fist Into It"
        elif activity_name == "Putting the Cart Before the Ferris":
            activity_name = "Putting the Cart Before the Ferris Wheel"
        elif activity_name == "Wheel What’s Your Cosine?":
            activity_name = "What’s Your Cosine?"
        elif activity_name == "Reference: A χ Probability Table":
            activity_name = "Reference: A χ2 Probability Table"
        elif activity_name == "On Tour with χ":
            activity_name = "On Tour with χ2"
        elif activity_name == "Measuring Weirdness with χ":
            activity_name = "Measuring Weirdness with χ2"
        elif activity_name == "χ for Dice":
            activity_name = "χ2 for Dice"
        elif activity_name == "A Mini Orchard":
            activity_name = "A Mini-Orchard"
        elif activity_name == "An Angle Summary":
            activity_name = "An Angular Summary"
        elif activity_name == "The Standard POW Write-up":
            activity_name = "Reference: The Standard POW Write-up"
        elif activity_name == "Sin, Cos, and Tan Revealed":
            activity_name = "Reference: Sin, Cos, and Tan Revealed"
        elif activity_name == "To Kearny by Equation":
            activity_name = "To Kearney by Equation"
        elif activity_name == "Reference: Approaching Infinity":
            activity_name = "Approaching Infinity"
        if len(activity_name) > 0:
            if not activity_name[0].isnumeric():
                if activity_name.startswith("Meaningful Math") or activity_name.startswith("©") or \
                        activity_name.startswith("i") or activity_name.startswith("Activity Notes"):
                    pass
                else:
                    print(activity_name, current_unit)
                    order_count += 1
                    units[current_unit]['activities'][activity_name] = {"order": order_count, "content": ""}

                    if len(first_activity_name) == 0:
                        first_activity_name = activity_name
                    activity_count += 1
            else:
                pass
        else:
            pass

    # if unit_name == "Is There Really a Difference":
    #     for a in all_activities_dict[unit_name]:
    #         print(a)
    #     quit()

    for activity in units[current_unit]['activities']:
        all_text_split = all_pdf_text.split("\n")
        activity_found = False
        row_num = 0
        for row_num in range(0, len(all_text_split)):
            line = all_text_split[row_num].strip()
            if not activity_found:
                if line.startswith(activity):
                    activity_found = True
            else:
                next_activity_num = units[current_unit]['activities'][activity]["order"] + 1
                next_activity = "Blackline Master"
                if current_unit == "Do Bees Build It Best?":
                    next_activity = "Do Bees Build It Best? Guide for the"
                elif current_unit == "Fireworks":
                    next_activity = "In-Class Assessment"
                elif current_unit == "How Much? How Fast?":
                    next_activity = "Zero to Sixty"
                for n_act in units[current_unit]['activities']:
                    if units[current_unit]['activities'][n_act]['order'] == next_activity_num:
                        next_activity = n_act
                if len(next_activity) > 10:
                    next_activity = next_activity[:10]

                if line.startswith("Intent"):
                    at_end = False
                    content = ""
                    while not at_end:
                        row_num += 1
                        try:
                            line = all_text_split[row_num].strip()
                        except IndexError:
                            print(activity)
                            print(next_activity)
                            quit()

                        if line.startswith(next_activity) or line.replace("’", "'").startswith(next_activity):
                            units[current_unit]['activities'][activity]["content"] = content.strip().lower()
                            content = ""
                            at_end = True
                        else:
                            if line.startswith("Meaningful Math"):
                                pass
                            elif line.startswith("©"):
                                pass
                            else:
                                # if next_activity == "Movin’ On":
                                #     print(line.strip())
                                content += line.strip() + " "
                    break  # break out of for loop
                else:
                    activity_found = False

    #get info on supplemental activities...
    # start = all_pdf_text.find("Reinforcements")
    # end = all_pdf_text.find(first_activity_name, start)
    # supplemental_split = all_pdf_text[start: end].split('\n')
    # description = ""
    # current_activity = ""
    # for raw_supplemental_name in supplemental_split:
    #     supplemental_name = raw_supplemental_name.strip()
    #     if len(supplemental_name) > 0:
    #         if "(reinforcement)" in supplemental_name or "(extension)" in supplemental_name:
    #             name_end = supplemental_name.find(")")
    #             name = supplemental_name[:name_end + 1]
    #
    #             units[current_unit]['activities'][name] = {"intent": "", "mathematics": "", "progression": ""}
    #             activity_count += 1
    #             current_activity = name
    #             if len(description) > 0:
    #                 # print(name)
    #                 # print(description)
    #                 # print()
    #                 if "reinforcement" in name and "extension" in name:
    #                     all_activities_dict[unit_name][name]["intent"] = "reinforcement and extension"
    #                 elif "reinforcement" in name:
    #                     all_activities_dict[unit_name][name]["intent"] = "reinforcement"
    #                 elif "extension" in name:
    #                     all_activities_dict[unit_name][name]["intent"] = "extension"
    #                 else:
    #                     all_activities_dict[unit_name][name]["intent"] = "unknown"
    #
    #                 all_activities_dict[unit_name][name]["mathematics"] = description.strip().lower()
    #                 all_activities_dict[unit_name][name]["progression"] = "supplemental"
    #             description = supplemental_name[name_end + 2:].strip()
    #         else:
    #             if supplemental_name.startswith("Meaningful Math"):
    #                 pass
    #             elif supplemental_name.startswith("©"):
    #                 pass
    #             elif supplemental_name.startswith("x"):
    #                 pass
    #             elif current_activity:
    #                 description += supplemental_name.strip()
    #             else:
    #                 pass

    #break #only do one unit


# input a list of keywords from a txt file
keyword_dict = {}
keyword_file = Path.cwd() / 'IMP Keywords.txt'
keywords = keyword_file.read_text().split("\n")
for k in keywords:
    key_line = k.split(',')
    keyword_dict[key_line[0]] = {"related": [], "activities": {}}
    if len(key_line) > 1:
        keyword_dict[key_line[0]]["related"] = key_line[1:]
    else:
        keyword_dict[key_line[0]]["related"] = []


# analyze all_activities_dict
for unit in units:
    for activity in units[unit]['activities']:
        for keyword in keyword_dict:
            all_keys = [keyword] + keyword_dict[keyword]["related"]
            for k in all_keys:
                if k in units[unit]['activities'][activity]["content"]:
                    if activity not in keyword_dict[keyword]["activities"]:
                        keyword_dict[keyword]["activities"][activity] = unit
                else:
                    pass

print(activity_count)

hierarchy_csv_path = Path.cwd() / "IMP Hierarchy.csv"
hierarchy_csv_path.write_text('')
hierarchy_csv = hierarchy_csv_path.open('a')

hierarchy_csv.write('Keyword,Year,Unit,Activity,Activity Count\n')
for k in keyword_dict:
    for activity in keyword_dict[k]["activities"]:
        write_unicode = f"{k}, Year {units[keyword_dict[k]['activities'][activity]]['year']}, " \
                        f"{keyword_dict[k]['activities'][activity]}, {activity.replace(',', '')}, " \
                        f"{str(len(keyword_dict[k]['activities']))}\n"
        string_encode = write_unicode.encode("ascii", "ignore")
        string_decode = string_encode.decode()
        hierarchy_csv.write(string_decode)

hierarchy_csv.close()


# keyword over time (putting units in order) - line chart, color code dots by uni
key_vs_time_csv_path = Path.cwd() / "IMP Keyword Count vs Activity Count.csv"
key_vs_time_csv_path.write_text('')
key_vs_time_csv = key_vs_time_csv_path.open('a')

key_count_temp_dict = {}
for k in keyword_dict:
    key_count_temp_dict[k] = len(keyword_dict[k]['activities'])

ordered_keywords = dict(sorted(key_count_temp_dict.items(), key=lambda item: item[1], reverse=True))
key_count_dict = {}
header_string = 'Activity Number,Year,Unit,Activity Name'
for k in ordered_keywords:
    header_string = header_string + ',' + k
    key_count_dict[k] = 0
key_vs_time_csv.write(header_string + '\n')

activity_count = 0
for unit_name in units:
    for year in range (1, 5):
        if units[unit_name]['year'] == year:
            for activity_name in units[unit_name]['activities']:
                line_string = f"{str(activity_count)},Year {year},{unit_name},{activity_name.replace(',', '')}"
                activity_count += 1
                for keyword in ordered_keywords:
                    if activity_name in keyword_dict[keyword]['activities']:
                        key_count_dict[keyword] += 1
                    line_string += ',' + str(key_count_dict[keyword])
                write_unicode = line_string + '\n'
                string_encode = write_unicode.encode("ascii", "ignore")
                string_decode = string_encode.decode()
                key_vs_time_csv.write(string_decode)


