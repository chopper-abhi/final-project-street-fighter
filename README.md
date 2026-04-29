Description
BASIC DESCRIPTION:
Street Fighter: a 2-player game where you control a stick figure delivering animated punches, kicks, and special attacks to the other player. The goal is to bring their health down to 0 and win the game.

DETAILED DESCRIPTION:
This program is an adaptation of Street Fighter using two differently colored stick figures (instead of two muscular, extremely-difficult-to-animate men), controlled by two users with a specific set of controls for each.
When it is run, the program displays the game screen, which has the basic grid background from Street Fighter 6. Two stick figures on opposite sides of the screen stand idle, their full health bars above them both.
Gameplay:
Player One, red and on the left, uses A and D to move, W to jump, 1 to punch, S to block, 2 to kick, and 3 for a special attack.
Player Two, blue and on the right, uses the left and right arrows to move, the up arrow to jump, 8 to punch, the down arrow to block, 9 to kick, and 0 for a special attack.
Both users can move their characters at the same time, unless they are directly next to one another (then, motion is prevented through collision detection).
All attacks which successfully land on the opponent reduce the opponent’s health, which updates live on the health bar.
A punch deals 5% damage, but its damage is nullified if the other opponent is in a block stance while receiving the punch.
Entering the block stance stops your motion, but not the motion of the other player. (Potential enhancement:) You can only block for a maximum of 5 seconds at a time, with a buffer of 5 seconds in between.
A kick deals 7% damage and breaks through a block, but it only deals damage if used in the air (due to having jumped prior to kicking).
A special attack deals 15% damage, and can be used when the attacker has dealt 5 punch/kick attacks. This is measured by the combo counter, which is reset to 0 after every special attack, regardless of its value.
When one player brings the opponent’s health bar to 0, a message is shown stating “Player _ Wins!” and gameplay ends.

Technology
Python, Pygame

Features that WILL be included
Game Screen:
User-controlled Stick Figures
Collision Detection
Health Bars
Punch Animations
Kick Animations
“Player _ Wins!” Text
Block Animations
Special Attack Animations
Combo Counters

Features that MUST be included
(P1) Game Screen:
(P1) User-controlled Stick Figures
(P1) Collision Detection
(P1) Health Bars
(P1) Punch Animations
(P1) Kick Animations
(P1) “Player _ Wins!” Text (printed is P1, displayed is P2)
(P2) Block Animations
(P2) Special Attack Animations
(P2) Combo Counters
