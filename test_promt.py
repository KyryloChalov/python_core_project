# from prompt_toolkit import prompt

# text = prompt("Give me some input: ")
# print("You said: %s" % text)



# def example_3():
#     """
#     Using ANSI for the formatting.
#     """
#     answer = prompt(
#         ANSI(
#             "\x1b[31mjohn\x1b[0m@"
#             "\x1b[44mlocalhost\x1b[0m:"
#             "\x1b[4m/user/john\x1b[0m"
#             "# "
#         )
#     )
#     print("You said: %s" % answer)

# example_3


# def get_session_token_with_mfa(self, client):
#     token_code = prompt("Please enter your MFA Token: ")
#     response = client.get_session_token(
#         DurationSeconds=config(
#             "assume_role_session_duration", default="3600", namespace="ssm_acquire"
#         ),
#         SerialNumber=config(
#             "mfa_serial_number", namespace="ssm_acquire", default="None"
#         ),
#         TokenCode=token_code,
#     )
#     return response
