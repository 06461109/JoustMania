![Magfest 2017](logo/magfest.jpg)
JoustMania at Magfest 2017!
![PiParty Logo](logo/PiPartyLogo2.png)

What is JoustMania????
--------------------------------------

* JoustMania is a collection of PlayStation Move enabled party games based off of the "Jostling" mechanic introduced in [Johann Sebastian Joust](http://www.jsjoust.com/)
* this collection of games attempts to expand upon JS Joust with new modes, as well as entirely new games, a platform for experimentation. 
* JoustMania is also designed to be easy to set up at conventions and is made to run itself with a large group of people. In convention mode, every game is started once everyone is ready, and announces the rules aloud for new players to learn.

Awesome Features!!
--------------------------------------

* 16+ Player support
* Super easy setup
* Runs in Headless mode, no screen required
* Multi game support, go beyond the standard Joust game, with team battles, werewolf, zombies, and commander mode
* Custom music support, play with your own music
* Convention mode, no manual instructions needed, the game plays itself and switches between game modes

Hardware
---------------------------
You will need the following to run JoustMania:

0. A Raspberry Pi 3 B with sd card
0. External USB sound card (https://goo.gl/S4vDXF)

Optional and **highly recommended**:

* Class 1, Bluetooth 4.0 USB adapters (https://goo.gl/q0j0Fu)

Note on Hardware: The internal bluetooth is short range and has a high latency, making gameplay laggy and slow, although still possible.
The class 1 adapters allow bluetooth connections up to 300+ feet and allow for the gameplay to be smooth, each adapter can connect to 6 to 7 controllers. I've tested this build with three adapters and 16 controllers successfully.

Optional:

* USB hub for charging controllers (https://www.amazon.com/dp/B00POYDAGS/)

This will allow you to charge 9 controllers at once through the pi

Installation
---------------------------

0. [Download](https://www.raspberrypi.org/downloads/raspbian/) and [Install](https://www.raspberrypi.org/documentation/installation/installing-images/README.md) Raspbian on the micro SD card
0. Connect the USB Soundcard and bluetooth adapters
0. Turn on the pi, open a Terminal and run these commands, the pi will reboot on a successful install
```
git clone https://github.com/adangert/JoustMania.git
cd JoustMania
sudo ./setup.sh
```
If you have the bluetooth adapters, disable the on-board bluetooth 
```
sudo ./disable_internal_bluetooth.sh
```
You can now disconnect the hdmi cable and run JoustMania in headless mode. JoustMania will automatically boot up on restart.


Pairing controllers
---------------------------

* Once you have installed JoustMania, in order to pair controllers, plug them into the Raspberry Pi via USB
* After a controller has been synced via USB, press the PlayStation sync button (the circular one in the middle) to connect the controller to the Pi
* This process should only need to be done once, after this the controller should be permenently paired with the Pi and will only need to be turned on via the sync button for any future games
* All the controllers may restart when pairing, this is expected, just keep plugging in new ones until they are all paired. if you encounter problems restart the Pi, and continue pairing the remaining controllers, again once this process is finished you should not have to connect the controllers to the Pi again via USB

If pairing is not working for some reason, or you would like to resync all controllers run the following
```
sudo ./reset_bluetooth_connections.sh
```

How to select a game mode
---------------------------------
* In order to change between games, on any controller press the select button (located on the left side of a controller)
* Changing game types will turn you into an Admin
* Press start (located on the right side) on any controller to launch the selected game
* In order to remove a controller from play press all four front buttons

Admin Mode (Sensitivity and convention mode settings)
---------------------------------
You can become an Admin by changing the game mode via the select button, this will allow you to modify the games settings from the four front buttons on the controller, After a game is played the Admin mode will be reset

* (Cross) Add or remove a game from Convention mode, your controller will be green if the game is added and Red if it is not, Custom Teams mode can not be added to the Convention mode
* (Circle) Change sensitivity of the game. There are three settings, slow, medium, and fast, you will hear a corresponding sound for each
* (Square) toggle the playback of instructions for each game
* (Triangle) show battery level on all controllers

Custom Music
---------------------------------
* JoustMania comes with a single classical music piece
* Play your own music, by copying it into the respective folders: /audio/(Joust, Zombie, Commander)/music/
* WAV files currently supported

Joust
---------------------------------
* Based off of the original [JS Joust](http://www.jsjoust.com/)
* Keep your controller still while trying to jostle others.
* If your controller is jostled then you are out of the game
* The music is tied to the gameplay, the faster the music the faster you can move

 Convention/Random mode
 ---------------------------------
 * This is the first mode that JoustMania boots to
 * This mode allows for multiple game types to be randomly rotated with instructions played before each game
 * Convention mode will only start with FFA in rotation, more game modes can be added as an Admin (see above)
 * All players press the A button (middle of controller) to signal they are ready to play, and the game will begin

 FFA (all controllers are white)
 ---------------------------------
 * The most basic version of Joust; be the last one standing!

 Teams (all controllers are solid colors)
 ---------------------------------
 * This game is the same as Joust FFA however at the beginning players select their team color with the big button in the middle of their controller
 * There are six teams to select from

 Random Teams (all controllers changing colors)
 ---------------------------------
 * Same as Joust Teams, however the teams are randomly assigned at start of play
 * There are three teams in this mode

 Werewolfs (one controller red, the rest white)
 ---------------------------------
 * Hidden werewolfs are selected at the beginning of the game.
 * When the countdown starts the werewolf will feel a vibration, letting that player know they are a werewolf
 * After a short period of time, werewolfs will be revealed
 * The Werewolfs only if they are the last remaining

 Zombie apocalypse
 ---------------------------------
 * Two players start out as zombies, and try to infect the humans
 * Humans can shoot random zombies with bullets
 * Bullets are randomly assigned as loot from killing zombies
 * Humans try to survive for a couple of minutes, otherwise zombies win!
 
 Commander
 ---------------------------------
 * Teams are split into two sides
 * One commander is chosen for each side, if this commander dies, the other team wins
 * Commanders can activate special abilities that helps their team win

  Ninja Bomb
  ---------------------------------
  * players sit in a circle each holding a controller
  * once everyone is in order, all players can press A to start the game. 
  * a bomb is passed around, by pressing the A button, if held too long it will explode
  * players can try to pass a fake bombs in order to make their opponents explode.
  * If a player presses A or trigger while holding a fake bomb, they explode
  * fake bombs are passed by holding the trigger-button half way, too much or too little and you'll give yourself away
  * fake bombs can be countered by pressing any of the four front buttons.
  * last player remaining wins!
 

 
  Swaper (coming soon)
  ---------------------------------
  * Players start on two teams
  * When you die, you switch to the other team
  * The last person remaining does not switch
  

