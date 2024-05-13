import statbotics
import requests

auth_TBA = {'X-TBA-Auth-Key' : '319O7fm4AYptga0ktUY6oIW4uLfUqatprLsxyyFkymObLkYbo7u4lSi8jJ9UJT3f'}

sb = statbotics.Statbotics()

match_list = requests.get(f'https://www.thebluealliance.com/api/v3/team/frc254/event/2024cada/matches/simple', params = auth_TBA).json()

updated_match_list = []
for match in match_list:
    if match['comp_level'] == 'qm':
        updated_match_list.append(match)

match_list = updated_match_list

print(sb.get_team_event(254, '2024cabe', fields = ['epa_pre_playoffs'])['epa_pre_playoffs'])
print(sb.get_team_event(1678, '2024cabe', fields = ['epa_pre_playoffs'])['epa_pre_playoffs'])
print(sb.get_team_event(1160, '2024cabe', fields = ['epa_pre_playoffs'])['epa_pre_playoffs'])