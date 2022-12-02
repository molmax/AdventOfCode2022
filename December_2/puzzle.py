opponent_rock = 'A'
opponent_paper = 'B'
opponent_scissors = 'C'
player_rock = 'X'
player_paper = 'Y'
player_scissors = 'Z'

def get_points_for_choice(player_choice):
    if player_choice == player_rock:
        return 1
    elif player_choice == player_paper:
        return 2
    elif player_choice == player_scissors:
        return 3


def get_points_for_result_pt1(opponent_choice, player_choice):
    points_for_outcome = 0

    draw_cond_1 = opponent_choice == opponent_rock and player_choice == player_rock
    draw_cond_2 = opponent_choice == opponent_paper and player_choice == player_paper
    draw_cond_3 = opponent_choice == opponent_scissors and player_choice == player_scissors

    if draw_cond_1 or draw_cond_2 or draw_cond_3:
        points_for_outcome = 3

    win_cond_1 = opponent_choice == opponent_rock and player_choice == player_paper
    win_cond_2 = opponent_choice == opponent_paper and player_choice == player_scissors
    win_cond_3 = opponent_choice == opponent_scissors and player_choice == player_rock

    if win_cond_1 or win_cond_2 or win_cond_3:
        points_for_outcome = 6

    return points_for_outcome + get_points_for_choice(player_choice)


def get_points_for_result_pt2(opponent_choice, how_round_should_end):
    points_for_outcome = 0
    if how_round_should_end == 'X':
        # Player should lose
        if opponent_choice == opponent_rock:
            player_choice = player_scissors
        elif opponent_choice == opponent_paper:
            player_choice = player_rock
        elif opponent_choice == opponent_scissors:
            player_choice = player_paper
    elif how_round_should_end == 'Y':
        # Draw
        points_for_outcome = 3
        if opponent_choice == opponent_rock:
            player_choice = player_rock
        elif opponent_choice == opponent_paper:
            player_choice = player_paper
        elif opponent_choice == opponent_scissors:
            player_choice = player_scissors
    elif how_round_should_end == 'Z':
        # Player should win
        points_for_outcome = 6
        if opponent_choice == opponent_rock:
            player_choice = player_paper
        elif opponent_choice == opponent_paper:
            player_choice = player_scissors
        elif opponent_choice == opponent_scissors:
            player_choice = player_rock

    return points_for_outcome + get_points_for_choice(player_choice)


def calculate_points_for_round(part):
    player_total_score = 0

    with open('input-data.txt', 'r') as file:
        for line in file:
            player_current_score = 0
            arg1 = line[0]
            arg2 = line[2]
            if part == 1:
                player_current_score += get_points_for_result_pt1(arg1, arg2)
            elif part == 2:
                player_current_score += get_points_for_result_pt2(arg1, arg2)
            player_total_score += player_current_score

    return player_total_score

def solution():
    result_pt1 = calculate_points_for_round(part = 1)
    result_pt2 = calculate_points_for_round(part = 2)
    return result_pt1, result_pt2

result_pt1, result_pt2 = solution()
print('result_pt1: ', result_pt1)
print('result_pt2: ', result_pt2)
