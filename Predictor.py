def main():
    # Ask for the player's position (Q for Quarterback, W for Wide Receiver, R for Running Back)
    position = input("Enter the player's position (Q for Quarterback, W for Wide Receiver, R for Running Back): ").upper()

    if position == "Q":
        # Ask if they have a list of yards or want to input them one by one
        input_method_qb = input("Do you have a list of yards thrown by the quarterback separated by commas (Y/N)? ").lower()
        if input_method_qb == "y":
            # Input the list of yards thrown by the quarterback separated by commas
            yards_qb_str = input("Enter the yards thrown by the quarterback for the last 5 games separated by commas: ")
            yards_qb_list = [float(yard) for yard in yards_qb_str.split(",")]
        elif input_method_qb == "n":
            # Input the quarterback's yards one by one
            num_games_qb = 5
            yards_qb_list = []

            print("Enter the yards thrown by the quarterback for the last 5 games:")
            for i in range(num_games_qb):
                yards_qb = float(input(f"Game {i + 1}: "))
                yards_qb_list.append(yards_qb)
        else:
            print("Invalid input method. Please enter Y or N.")
            return

        # Ask if they have a list of yards given up by the opposing team or want to input them one by one
        input_method_opposing = input("Do you have a list of yards given up by the opposing team separated by commas (Y/N)? ").lower()
        if input_method_opposing == "y":
            # Input the list of yards given up by the opposing team separated by commas
            yards_given_up_str = input("Enter the yards given up by the opposing team for the last 5 games separated by commas: ")
            yards_given_up_list = [float(yard) for yard in yards_given_up_str.split(",")]
        elif input_method_opposing == "n":
            # Input the yards given up by the opposing team one by one
            num_games_opposing = 5
            yards_given_up_list = []

            print("Enter the yards given up by the opposing team for the last 5 games:")
            for i in range(num_games_opposing):
                yards_given_up = float(input(f"Game {i + 1}: "))
                yards_given_up_list.append(yards_given_up)
        else:
            print("Invalid input method. Please enter Y or N.")
            return

        # Calculate the estimated yards as the midpoint
        estimated_yards = (sum(yards_qb_list) + sum(yards_given_up_list)) / (len(yards_qb_list) + len(yards_given_up_list))

        # Calculate the average yards thrown by the quarterback
        average_yards_qb = sum(yards_qb_list) / len(yards_qb_list)

        # Calculate the difference in yards between QB and Defense
        yard_difference = abs(average_yards_qb - sum(yards_given_up_list) / len(yards_given_up_list))

        # Determine whether to increase or decrease estimated yards
        if average_yards_qb < sum(yards_given_up_list) / len(yards_given_up_list):
            # Quarterback yards less than opposing yards
            if yard_difference >= 75:
                estimated_yards += (estimated_yards * 0.25)  # Increase by 25%
            elif 50 <= yard_difference < 75:
                estimated_yards += (estimated_yards * 0.15)  # Increase by 15%
            elif yard_difference < 50:
                estimated_yards += (estimated_yards * 0.05)  # Increase by 5%
        elif average_yards_qb > sum(yards_given_up_list) / len(yards_given_up_list):
            # Quarterback yards more than opposing yards
            if yard_difference >= 75:
                estimated_yards -= (estimated_yards * 0.25)  # Decrease by 25%
            elif 50 <= yard_difference < 75:
                estimated_yards -= (estimated_yards * 0.15)  # Decrease by 15%
            elif yard_difference < 50:
                estimated_yards -= (estimated_yards * 0.05)  # Decrease by 5%

    elif position == "W":
        # Ask if they are a WR1, WR2, or WR3
        receiver_type = input("Enter the receiver type (WR1, WR2, or WR3): ").lower()
        # Ask for the number of yards thrown by the quarterback in the same way as for the quarterback position
        input_method_qb = input("Do you have a list of yards thrown by the quarterback separated by commas (Y/N)? ").lower()
        if input_method_qb == "y":
            yards_qb_str = input("Enter the yards thrown by the quarterback for the last 5 games separated by commas: ")
            yards_qb_list = [float(yard) for yard in yards_qb_str.split(",")]
        elif input_method_qb == "n":
            num_games_qb = 5
            yards_qb_list = []

            print("Enter the yards thrown by the quarterback for the last 5 games:")
            for i in range(num_games_qb):
                yards_qb = float(input(f"Game {i + 1}: "))
                yards_qb_list.append(yards_qb)
        else:
            print("Invalid input method. Please enter Y or N.")
            return

        # Ask if they have a list of yards given up by the opposing team or want to input them one by one
        input_method_opposing = input("Do you have a list of yards given up by the opposing team separated by commas (Y/N)? ").lower()
        if input_method_opposing == "y":
            # Input the list of yards given up by the opposing team separated by commas
            yards_given_up_str = input("Enter the yards given up by the opposing team for the last 5 games separated by commas: ")
            yards_given_up_list = [float(yard) for yard in yards_given_up_str.split(",")]
        elif input_method_opposing == "n":
            # Input the yards given up by the opposing team one by one
            num_games_opposing = 5
            yards_given_up_list = []

            print("Enter the yards given up by the opposing team for the last 5 games:")
            for i in range(num_games_opposing):
                yards_given_up = float(input(f"Game {i + 1}: "))
                yards_given_up_list.append(yards_given_up)
        else:
            print("Invalid input method. Please enter Y or N.")
            return

        # Calculate the estimated yards as the midpoint
        estimated_yards = (sum(yards_qb_list) + sum(yards_given_up_list)) / (len(yards_qb_list) + len(yards_given_up_list))

        # Calculate the difference in yards between WR and Defense
        yard_difference = abs(average_yards_qb - sum(yards_given_up_list) / len(yards_given_up_list))

        # Determine whether to increase or decrease estimated yards
        if average_yards_qb < sum(yards_given_up_list) / len(yards_given_up_list):
            # Wide Receiver yards less than opposing yards
            if yard_difference >= 30:
                estimated_yards += (estimated_yards * 0.20)  # Increase by 20%
            elif 20 <= yard_difference < 30:
                estimated_yards += (estimated_yards * 0.125)  # Increase by 12.5%
            elif yard_difference < 20:
                estimated_yards += (estimated_yards * 0.05)  # Increase by 5%
        elif average_yards_qb > sum(yards_given_up_list) / len(yards_given_up_list):
            # Wide Receiver yards more than opposing yards
            if yard_difference >= 30:
                estimated_yards -= (estimated_yards * 0.20)  # Decrease by 20%
            elif 20 <= yard_difference < 30:
                estimated_yards -= (estimated_yards * 0.125)  # Decrease by 12.5%
            elif yard_difference < 20:
                estimated_yards -= (estimated_yards * 0.05)  # Decrease by 5%

        # Adjust based on receiver type
        if receiver_type == "wr1":
            estimated_yards *= 0.20
        elif receiver_type == "wr2":
            estimated_yards *= 0.25
        elif receiver_type == "wr3":
            estimated_yards *= 0.35
        else:
            print("Invalid receiver type. Please enter WR1, WR2, or WR3.")
            return

    elif position == "R":
        # Ask if they have a list of yards given up by the opposing team or want to input them one by one
        input_method_opposing = input("Do you have a list of yards given up by the opposing team separated by commas (Y/N)? ").lower()
        if input_method_opposing == "y":
            # Input the list of yards given up by the opposing team separated by commas
            yards_given_up_str = input("Enter the yards given up by the opposing team for the last 5 games separated by commas: ")
            yards_given_up_list = [float(yard) for yard in yards_given_up_str.split(",")]
        elif input_method_opposing == "n":
            # Input the yards given up by the opposing team one by one
            num_games_opposing = 5
            yards_given_up_list = []

            print("Enter the yards given up by the opposing team for the last 5 games:")
            for i in range(num_games_opposing):
                yards_given_up = float(input(f"Game {i + 1}: "))
                yards_given_up_list.append(yards_given_up)
        else:
            print("Invalid input method. Please enter Y or N.")
            return

        # Ask if they have a list of yards thrown by the quarterback or want to input them one by one
        input_method_qb = input("Do you have a list of yards thrown by the quarterback separated by commas (Y/N)? ").lower()
        if input_method_qb == "y":
            # Input the list of yards thrown by the quarterback separated by commas
            yards_qb_str = input("Enter the yards thrown by the quarterback for the last 5 games separated by commas: ")
            yards_qb_list = [float(yard) for yard in yards_qb_str.split(",")]
        elif input_method_qb == "n":
            # Input the yards thrown by the quarterback one by one
            num_games_qb = 5
            yards_qb_list = []

            print("Enter the yards thrown by the quarterback for the last 5 games:")
            for i in range(num_games_qb):
                yards_qb = float(input(f"Game {i + 1}: "))
                yards_qb_list.append(yards_qb)
        else:
            print("Invalid input method. Please enter Y or N.")
            return

        # Calculate the estimated yards as the midpoint
        estimated_yards = (sum(yards_qb_list) + sum(yards_given_up_list)) / (len(yards_qb_list) + len(yards_given_up_list))

        # Calculate the difference in yards between RB and Defense
        yard_difference = abs(average_yards_qb - sum(yards_given_up_list) / len(yards_given_up_list))

        # Determine whether to increase or decrease estimated yards
        if average_yards_qb < sum(yards_given_up_list) / len(yards_given_up_list):
            # Running Back yards less than opposing yards
            if yard_difference >= 35:
                estimated_yards += (estimated_yards * 0.20)  # Increase by 20%
            elif 24 <= yard_difference < 35:
                estimated_yards += (estimated_yards * 0.125)  # Increase by 12.5%
            elif yard_difference < 24:
                estimated_yards += (estimated_yards * 0.05)  # Increase by 5%
        elif average_yards_qb > sum(yards_given_up_list) / len(yards_given_up_list):
            # Running Back yards more than opposing yards
            if yard_difference >= 35:
                estimated_yards -= (estimated_yards * 0.20)  # Decrease by 20%
            elif 24 <= yard_difference < 35:
                estimated_yards -= (estimated_yards * 0.125)  # Decrease by 12.5%
            elif yard_difference < 24:
                estimated_yards -= (estimated_yards * 0.05)  # Decrease by 5%

    else:
        print("Invalid position. Please enter Q for Quarterback, W for Wide Receiver, or R for Running Back.")

    # Print the estimated yards
    print(f"Estimated Yards: {estimated_yards:.2f}")

if __name__ == "__main__":
    main()
