
# One-Time Password (OTP)

[[🏷️Authentication methods]]

A common implementation of a second factor is the use of one-time passwords (OTP). One-time passwords are an important way to combat password theft and other password-based attacks. As its name implies, a one-time password is usable only once. An attacker can obtain a one-time password but cannot continue using it, and it means that brute-force attacks will be constantly attempting to identify a constantly changing target. Though it is possible that a brute-force attack could randomly match a one-time password during the time that it is valid, the likelihood of an attack like that succeeding is incredibly small, and common controls that prevent brute-force attacks will make that type of success essentially impossible.

There are two primary models for generation of one-time passwords. The first is time-based one-time passwords (TOTP), which use an algorithm to derive a one-time password using the current time as part of the code-generation process. Authentication applications like Google Authenticator use TOTP, as shown in [[Image 2.60.png|Image 2.60]]. The code is valid for a set period of time and then moves on to the next time-based code, meaning that even if a code is compromised it will be valid for only a relatively short period of time.

![[Image 2.60.png]]

The codes shown are valid for a set period of time, shown by the animation of a pie chart in the bottom-right corner, and in the application they turn red as they are about to expire and be replaced with a new code.

The other one-time password generation model is HMAC-based one- time password (HOTP). HMAC stands for hash-based message authentication codes. HOTP uses a seed value that both the token or HOTP code-generation application and the validation server use, as well as a moving factor. For HOTP tokens that work when you press a button, the moving factor is a counter, which is also stored on the token and the server. HOTP password generators, like the PayPal token shown in [[Image 2.61.png|Image 2.61]] rely on an event, such as pressing a button, to cause them to generate a code. Since the codes are iterative, they can be checked from the last known use of the token, with iterations forward until the current press is found. Like TOTP solutions, authentication applications can also implement HOTP and work the same way that a hardware token implementation does. 

![[Image 2.61.png]]

In addition to application and hardware tokens, a third common implementation of a one-time password system is the use of codes based on the short message service (SMS), or text message. In this model, when a user attempts to authenticate, an SMS message is sent to their phone, and they then input that code as an additional factor for the authentication process.

> [!warning] Attacking One-Time Passwords
> One-time passwords aren't immune to attack, although they can make traditional attacks on accounts that rely on acquiring passwords fail. TOTP passwords can be stolen by either tricking a user into providing them, gaining access to a device like a phone, where they are generated, or otherwise having near real-time access to them. This means that attackers must use a stolen TOTP password immediately. One-time passwords sent via SMS can be redirected using a cloned SIM, or if the phone is part of a VoIP network, by compromising the VoIP system or account and redirecting the SMS factor.
>
> Attacks against SMS OTP as well as application-based OTP are on the rise as malicious actors recognize the need to overcome multifactor authentication. For now, however, one of the most successful attacks is simply overwhelming end users with repeated validation requests so that they enter an OTP value to make the requests stop!

In situations where hardware and software tokens as well as SMS aren't suitable, some organizations will implement a phone call–based push notification. Push notifications are messages sent to a user to inform them of an event, in this case an authentication attempt. If users respond to the phone call with the requested validation— typically by pushing a specific button on the keypad—the authentication can proceed. Phone calls suffer from a number of issues as an authentication factor, including lower speed, which can cause issues with login timeouts; the potential for hijacking of calls via a variety of means; and additional costs for the implementing organization due to phone call costs. 

Although one-time passwords that are dynamically generated as they are needed are more common, at times, there is a need for a one-time password that does not require a device or connectivity. In those cases, static codes remain a useful option. Static codes are also algorithmically generated like other one-time passwords but are pre- generated and often printed or stored in a secure location. This creates a new risk model, which is that the paper they are printed on could be stolen, or if they are stored electronically, the file they're stored in could be lost or accessed. This would be equivalent to losing a button- press activated token or an unlocked smartphone, so static codes can be dangerous if they are not secured properly.


