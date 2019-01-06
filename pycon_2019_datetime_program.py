from datetime import date


def print_header():
    print("--------------------------------------")
    print("    PYCON 2019 DATETIME 100DoC APP")
    print("--------------------------------------")
    print()


def get_flight_date_from_user():
    print("When are you flying out for PYCON 2019? ")
    month = int(input("Month [MM]: "))
    day = int(input("Day [DD]: "))

    flight_date = date(2019, month, day)
    return flight_date


def calculate_timedelta(start_date, end_date):
    calculation = start_date - end_date
    return calculation.days


def print_flight_information(days):
    if days < 0:
        print(
            f"I hope you already made your flight to PYCON 2019! You should have flown out {-days} days ago!"
        )
    elif days == 1:
        print(
            f"Get your bags packed today if they aren't already! Your flight to PYCON 2019 is tomorrow! That's only {days} day!"
        )
    elif days > 0 and days < 7:
        print(
            f"Get your bags packed soon! Your flight to PYCON 2019 is in {days} days!"
        )
    elif days > 0:
        print(
            f"Spend some time writing Python before you pack your bags. Your flight to PYCON 2019 isn't for another {days} days."
        )
    else:
        print(
            "I hope you already packed your bags! Your flight out to PYCON 2019 is today! See you there!!!"
        )


def main():
    print_header()
    day_of_flight = get_flight_date_from_user()
    today = date.today()
    number_of_days = calculate_timedelta(day_of_flight, today)
    print_flight_information(number_of_days)


if __name__ == "__main__":
    main()
