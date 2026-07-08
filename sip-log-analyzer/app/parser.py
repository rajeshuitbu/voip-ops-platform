def parse_sip_log(filename):

    calls = {}

    current_method = None
    current_response = None

    with open(filename, "r") as file:

        for raw_line in file:

            line = raw_line.strip()

            if not line:
                continue

            # SIP Method
            if line.startswith(("INVITE", "REGISTER", "ACK",
                                "BYE", "OPTIONS", "CANCEL")):

                current_method = line.split()[0]
                current_response = None

            # SIP Response
            elif line.startswith(("100", "180", "183",
                                  "200", "401", "403",
                                  "404", "408", "480",
                                  "486", "487", "500",
                                  "503")):

                current_response = line.split()[0]
                current_method = None

            # Call-ID
            elif line.startswith("Call-ID:"):

                call_id = line.replace("Call-ID:", "").strip()

                if call_id not in calls:

                    calls[call_id] = {
                        "headers": {},
                        "call_flow": []
                    }

                if current_method:

                    calls[call_id]["call_flow"].append(current_method)

                elif current_response:

                    calls[call_id]["call_flow"].append(current_response)

            # From
            elif line.startswith("From:"):

                if call_id in calls:

                    calls[call_id]["headers"]["from"] = \
                        line.replace("From:", "").strip()

            # To
            elif line.startswith("To:"):

                if call_id in calls:

                    calls[call_id]["headers"]["to"] = \
                        line.replace("To:", "").strip()

            # User-Agent
            elif line.startswith("User-Agent:"):

                if call_id in calls:

                    calls[call_id]["headers"]["user_agent"] = \
                        line.replace("User-Agent:", "").strip()

    return calls
