import csv

from stats.models import teamData, clubName, ExtraData



def run():
    with open('stats.csv') as file:
        reader = csv.reader(file)
        next(reader)

        clubName.objects.all().delete()
        teamData.objects.all().delete()
        ExtraData.objects.all().delete()
        # Season.objects.all().delete()

        for row in reader:

            club_name, _ = clubName.objects.get_or_create(name=row[0])
            # season_period, _ = Season.objects.get_or_create(season=row[41])

            team_data = teamData(
                        wins=row[1],
                        losses=row[2],
                        goals=row[3],
                        teamName=club_name)
            team_data.save()

            extra_data = ExtraData(
                        yel_cards=row[4],
                        red_cards=row[5],
                        shots_att=row[6],
                        on_target_att=row[7],
                        woodwork=row[8],
                        header_goals=row[9],
                        penalty_goals=row[10],
                        freekick_goals=row[11],
                        ibox_goals=row[12],
                        obox_goals=row[13],
                        fastbreak_goals=row[14],
                        offsides=row[15],
                        zero_goals=row[16],
                        conceded_goals=row[17],
                        saves=row[18],
                        blocks=row[19],
                        interceptions=row[20],
                        tackles=row[21],
                        last_man_tackles=row[22],
                        clearances=row[23],
                        own_goals=row[24],
                        penalties_conceded=row[25],
                        goals_from_penalties=row[26],
                        passes=row[27],
                        long_balls=row[28],
                        crosses=row[29],
                        corners=row[30],
                        touches=row[31],
                        penalties_saved=row[32],
                        teamName=club_name)
            extra_data.save()

            # season = Season(
            #     season=season_period)
            # season.save()
