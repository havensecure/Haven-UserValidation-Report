import pandas as pd
from io import StringIO

# 1. Load your original dataset
original = pd.read_csv("Haven_Survey_Formatted_For_Form.csv")

# 2. Paste in your new TSV‐formatted block (tabs between columns)
new_data = """Timestamp	How often do you receive suspicious emails, texts, or scam links?	Have you (or someone close to you) ever fallen for a phishing or scam attempt?	When faced with a suspicious link or message, what do you usually do?	On a scale of 1–10, how safe do you feel online when browsing, messaging, or shopping?	Do you believe existing tools like antivirus apps or browser warnings are enough to protect people today?	What concerns you most when using your phone or laptop?	How valuable does that sound to you?	If this app existed, how likely are you to install it on your phone?	Which of these features would personally convince you to use it?	Would you be willing to pay for this app if it offered strong protection?	What pricing would feel fair for this kind of app?	What would make you trust a cybersecurity app enough to use it daily?	What tools do you currently use to stay safe online (if any)?	What’s the biggest frustration or fear you’ve had regarding your online security?	Want early access or to be part of our beta program?
4/15/2025 3:09:03	Weekly	Yes, I have	I’m not sure what to do	4	No, they’re outdated or reactive	Phishing or scam messages	Extremely valuable	Definitely	Real-time phishing detection, Security score with actionable tips, All of the above	Yes, monthly subscription	$10/month				Yes
4/15/2025 3:20:37	Weekly	Yes, someone close to me has	I’m not sure what to do	5	No, they’re outdated or reactive	Data leaks or hacks	Extremely valuable	Probably	All of the above	Maybe, depends on features	$10/month				Yes
4/16/2025 12:46:41	Weekly	Not sure	Ignore it	8	Yes, they’re sufficient	Identity theft	Somewhat valuable	Not sure	Dark web monitoring	No, I only use free tools	I wouldn’t pay	Free + more useful than existing solutions	Unlock, malwarebytes, common sense	Data breach from big companies that have your data	Maybe
4/17/2025 14:18:38	Rarely	Yes, someone close to me has	Ignore it	8	Somewhat, but there are gaps	Data leaks or hacks	Somewhat valuable	Not sure	SMS/email scanning for scams	Yes, one-time lifetime fee	$10/month				Maybe
4/24/2025 1:56:40	Daily	Yes, I have	I’m not sure what to do	3	Somewhat, but there are gaps	Phishing or scam messages	Extremely valuable	Definitely	Real-time phishing detection, Dark web monitoring, Security score with actionable tips, SMS/email scanning for scams, Privacy-first (on-device AI), Alerts about insecure apps or websites	Yes, monthly subscription	$2/month	Stopping scam msg	Nothing 	Scam msgs	Yes
4/24/2025 2:05:11	Daily	No, never	I’m not sure what to do	2	I don’t use any protection tools	Phishing or scam messages	Extremely valuable	Definitely	Real-time phishing detection	Maybe, depends on features	$2/month				Yes
4/24/2025 2:09:56	Occasionally	Yes, I have	Ignore it	5	Somewhat, but there are gaps	Financial fraud	Valuable	Probably	SMS/email scanning for scams, Privacy-first (on-device AI), Alerts about insecure apps or websites	Maybe, depends on features	$5/month		Nothing	Financial fraud	Maybe
4/24/2025 10:57:20	Weekly	Not sure	Ignore it	6	I don’t use any protection tools	Data leaks or hacks	Somewhat valuable	Not sure	Real-time phishing detection, SMS/email scanning for scams, Alerts about insecure apps or websites	No, I only use free tools	I wouldn’t pay	No memory consumption or no phone performance degrade	No	Data misuse	Maybe
4/24/2025 11:34:37	Daily	Not sure	Ignore it	3	Somewhat, but there are gaps	Phishing or scam messages	Somewhat valuable	Not sure	Alerts about insecure apps or websites	Maybe, depends on features	I wouldn’t pay	Normal phone for only talking purposes and separate device for other needs which are not accessible to everyone and restricted to reach only concern and limited contacts.	Using smartphone but only for talking purposes, I'm avoiding any personal important communication and transaction on phone.	We facing daily unwanted calls and offers that are not concerned with us, My personal details and thoughts are reaching to unknown people and companies.	Maybe
4/24/2025 13:29:49	Daily	Yes, someone close to me has	Ignore it	5	Somewhat, but there are gaps	Data leaks or hacks	Extremely valuable	Definitely	Real-time phishing detection	Maybe, depends on features	$2/month	Data privacy	Nothing	Don’t remember	Yes
4/24/2025 16:50:42	Daily	Yes, I have	Ignore it	3	No, they’re outdated or reactive	Financial fraud	Extremely valuable	Definitely	Privacy-first (on-device AI)	Yes, monthly subscription	$5/month	To safeguard myself from cyber crime’s abd fraud.	No tools	Data and privacy leak	Yes
4/25/2025 5:11:36	Rarely	Yes, I have	Ignore it	4	No, they’re outdated or reactive	Malware or viruses	Extremely valuable	Definitely	Security score with actionable tips, SMS/email scanning for scams, Alerts about insecure apps or websites	Yes, monthly subscription	$5/month			Data leaks and viruses	Maybe
4/25/2025 18:05:40	Rarely	Yes, someone close to me has	Try to verify manually (Google it, ask someone)	8	Somewhat, but there are gaps	Malware or viruses	Extremely valuable	Probably	Real-time phishing detection, Security score with actionable tips, SMS/email scanning for scams, Alerts about insecure apps or websites	No, I only use free tools	I wouldn’t pay				Maybe
4/26/2025 1:29:15	Weekly	Yes, I have	Ignore it	1	Yes, they’re sufficient	Data leaks or hacks	Extremely valuable	Probably	Real-time phishing detection	Yes, monthly subscription	$2/month				Yes
4/26/2025 1:30:55	Daily	Yes, I have	Ignore it	3	No, they’re outdated or reactive	Data leaks or hacks	Extremely valuable	Definitely	Dark web monitoring	Yes, monthly subscription	$10/month	Yes	No tools	Data leak	Yes
4/26/2025 1:41:31	Daily	Yes, I have	Use an antivirus or protection app	8	Yes, they’re sufficient	Malware or viruses	Extremely valuable	Definitely	Real-time phishing detection	Yes, monthly subscription	$10/month	Its reliability	Haven	Scam	Yes
4/26/2025 1:54:56	Rarely	Yes, someone close to me has	Try to verify manually (Google it, ask someone)	8	Somewhat, but there are gaps	Financial fraud	Extremely valuable	Definitely	All of the above	Yes, monthly subscription	$5/month	No, but still it will make a difference.	Secure web browser.	Money loss or identity theft.	Yes
4/26/2025 1:57:41	Daily	Yes, I have	Ignore it	5	No, they’re outdated or reactive	Malware or viruses	Valuable	Probably	Real-time phishing detection, Dark web monitoring, Security score with actionable tips, SMS/email scanning for scams, Privacy-first (on-device AI), Alerts about insecure apps or websites, All of the above	Yes, monthly subscription	$2/month	Accuracy and authenticity		Spam sms calls	Maybe
4/26/2025 2:46:33	Occasionally	Not sure	Use an antivirus or protection app	6	Somewhat, but there are gaps	Malware or viruses	Valuable	Definitely	Real-time phishing detection, Security score with actionable tips, SMS/email scanning for scams, Privacy-first (on-device AI), Alerts about insecure apps or websites	Maybe, depends on features	$5/month	Security	No	Malware	Maybe
4/26/2025 7:56:38	Occasionally	Yes, I have	Ignore it	8	Yes, they’re sufficient	Data leaks or hacks	Valuable	Probably	Real-time phishing detection, Dark web monitoring, Alerts about insecure apps or websites	No, I only use free tools	I wouldn’t pay				Yes
"""

# 3. Read new data in as a DataFrame
new_df = pd.read_csv(StringIO(new_data), sep="\t")

# 4. Concatenate and drop any exact duplicates
merged = pd.concat([original, new_df], ignore_index=True).drop_duplicates()

# 5. Write out a new master CSV
merged.to_csv("Haven_Survey_Formatted_For_Form_updated.csv", index=False)

print(f"Original rows: {len(original)}")
print(f"New rows:      {len(new_df)}")
print(f"Total now:     {len(merged)}")
