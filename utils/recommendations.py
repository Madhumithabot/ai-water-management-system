def get_recommendations(level):

    if level=="Low":
        return [
        "Maintain current water usage habits",
        "Encourage rainwater harvesting",
        "Monitor water usage regularly"
        ]

    elif level=="Medium":
        return [
        "Fix pipeline leaks",
        "Reduce unnecessary water usage",
        "Install water efficient appliances"
        ]

    else:
        return [
        "Install low-flow fixtures",
        "Adopt rainwater harvesting system",
        "Recycle greywater for gardening"
        ]