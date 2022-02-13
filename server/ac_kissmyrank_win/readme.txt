Kissmyrank Assetto Corsa Server Plugin - Racing the way it's meant to be
---------------------------------------------
Version: 1.6f
Author: Brioche
License: Free use and redistribution. No warranty. Use at your own risk. Modification/reuse of the code requires the author's permission.
---------------------------------------------
What it is and what it does
This is a simple self-contained Assetto Corsa Dedicated Server plugin (standalone exe) meant to promote knowledge of the gentlemen drivers' driving etiquette and fair racing.
Rather than trying to assess drivers' safety in funny ways (contact points, splits etc. which have no place in reality), this plugin replicates real racing dynamics by simulating the environmental conditions that occur in real life (damage, penalties etc.).
If you collide with another car in the real world, you will not get fancy contact points or weird safety ratings but just a penalty and you'll get to pay for the damage that you caused on your car. Same goes if you crash against a wall (regardless of the presence of other drivers).
This is the only realistic rating that can have place in a sim and what Kissmyrank tries to achieve.
On top of this, it adds a human control layer (just like real Race Control) where admins can enlist Race Officials to review replays and give penalties (drive-through, kick, temporary ban and/or money) simply using their Web Browser.
---------------------------------------------
League Racing and Private Servers
While the money/point system is useful to moderate public servers, it might be unnecessary for League Servers and Private Servers.
Admins can use the "jlp_money_kill_switch" config.json entry to disable the money system altogether and still use all the other Kissmyrank Race Control Monitoring, Drive-Through and Tracking features.
---------------------------------------------
Requirements
This plugin runs locally and doesn't need any remote master server to operate. If you can launch an exe then you're good to go.
There are no requirements at all except having an Assetto Corsa Dedicated Server. All the data is saved in the folder where you run the plugin and the only connection required is the one with the Assetto Corsa dedicated server.
---------------------------------------------
Disclaimer
The plugin might use, store and publicly display the players public IP, the Steam GUID and the in-game nickname. All data is stored locally on your server and it's under your exclusive responsibility. The plugin comes with absouletly no warranty regarding this or any other matter. In order to help you comply with local regulations, new players that leave the server before going to the track are not logged to the stats database. Kissmyrank also provides a "kmr erase_my_personal_data_and_ban_myself" chat command for those who had some data logged and wish to opt-out (set config entry #160 to 1 to enable it). You might, at your own discretion, add a Custom Welcome message (config entry #78) to notify your players about the treatment of their data and the options they have to opt-out.
---------------------------------------------
Features
- Live Track View (view real-time driving lines live on the map!)
- Live Race Control (Admins can view replays and moderate driver behavior using a Web Browser)
- Ping limit and ping stability check
- Standing Start
- Rolling Start with Formation Lap
- Virtual Safety Car (with autodeploy on mass accidents)
- Kissmyrank In-Game Spotter App: https://www.dropbox.com/s/aj01yjn6yl1vc4j/Kissmyrank_Spotter_App.zip?dl=0
- Win, Podiums, Poles, Fastest Laps, Driving infractions, Collisions tracking
- Custom Boundary definitions (include and exclude areas)
- Pit Lane Speed Limit definitions
- Pit Exit Line definitions
- Track map replays for cuts and collisions
- Drive-Through, Kick and Temporary Ban Penalties
- Multi-Language support (please help with translations!)
- Collision Damage
- Lapping and Hotlapping car warning and penalties
- Laptime Records tracking (using the custom track limits definitions)
- Laptime Challenge and Rewards
- Computer Clock Laptime Validator Anticheat (to filter some leaderboard exploits)
- Race Entry Fee (to responsibilize drivers) and prizes (also for fastest lap and qualify)
- Reward for laps without cuts
- Virtual Safety Car (or Automatic Race Restart) on first lap carnage
- Skips race if there are not enough players
- Pole announcement
- Race winner announcement
- First accident shame announcement
- Reverse Gear Penalty
- Max Infractions and Max Collisions
- Fastest lap of the race announcement
- Driving Standard (you can require times to be within a certain % of the leaderboard best)
- Restrict players with high collision rates
- Car Towing Cost
- Web Track Editor (for boundaries and such)
- Track Rotation
- Leaderboard
- Web Stats Server
- Race Results Viewer
- Assetto Corsa Auth Support (Web Auth Server)
- Auth Relay (to use external Auth like Minorating or Stracker)
- UDP Relay (to chain other plugins)
- Reserved Slots (join your server when it's full)
- Web Administrator Console (to manage the plugin and your Assetto Corsa server from your Web Browser)
- Send Console Commands from the Assetto Corsa Chat
- Temporary Ban
- Programmable Penalties via the Penalty Cost and Penalty Action maps
- Assetto Corsa App Link for sending Kissmyrank Events to in-game apps without using the chat
- No cumbersome/unrealistic/arcade class based approach which splits the driving community
- First Time SetupWizard (just extract the package and launch)
- Fully customizable plugin (more than 160 settings for you to play with)
---------------------------------------------
Download: https://www.dropbox.com/sh/7lp4mobixpdx7x3/AABWelmzZlJPysxnRwJK-DL4a?dl=0
---------------------------------------------
Installation
Extract files to any path.
---------------------------------------------
Runtime
Just launch the appropriate binary for your platform.
---------------------------------------------
Automatic Configuration:
Launch the plugin and run through the Setup Wizard.
The Setup Wizard will set the most important settings for you. Once you're done, you can customize the gameplay experience by manually editing the config.json file.
----------------------------------------------
Manual Configuration:
If you wish to perform the first time configuration manually, copy config.default.json to config.json.
Then edit config.json and:
1) set "ac_server_plugin_local_port" to the value that you set in the Assetto Corsa server_cfg.ini under UDP_PLUGIN_LOCAL_PORT (e.g for UDP_PLUGIN_LOCAL_PORT=8004 set it to 8004).
2) set "ac_server_plugin_address_port" according to the value that you set in server_cfg.ini for UDP_PLUGIN_ADDRESS (e.g for UDP_PLUGIN_ADDRESS=127.0.0.1:12000 set the "ac_server_plugin_address_port" to 12000). Please note that the IP that you should use in the server_cfg.ini is the one of the machine where you run ac_kissmyrank binary.
3) set "ac_server_ip" to the IP address of your Assetto Corsa Server (please ensure that you use the same interface that you used for the plugin).
4) set "ac_server_http_port" to match the Assetto Corsa server_cfg.ini HTTP_PORT setting.
5) set "max_players" according to the number of slots on your server.
6) if you need track rotation set the ac server path
---------------------------------------------
Commands
You can type commands in the Kissmyrank Plugin Console. You can use tab to autocomplete. Hit tab twice or write help for a list of commands.
---------------------------------------------
Kissmyrank Management Commands: help, clear, config_get, config_set, backup_list, backup_restore, save, exit");
~ help: shows a full list of commands (you can also get the full list by pressing tab twice)
~ help config_get: shows help for the config_get command
~ json_verify {"PRACTICE": "remove", "QUALIFY": {"TIME": 10}, "RACE": {"LAPS": 10}}: verifies if the provided string is valid JSON to be used for any command that requires this kind of format (e.g. track_rotation_edit)
~ config_get max_ping: gets the current value of the max_ping configuration entry
~ config_set id|value: sets the config_id config.json entry to value (please note how the value after | must be in the exact same format that you would get using the config_get command)
~ config_set max_ping|300: sets max_ping to 300 and saves the config.json
~ config_set currency_symbol|"$": sets the currency_symbol to "$" and saves the config.json
~ backup_list: lists the available backup dates to be used with the backup_restore command
~ backup_create: creates a new backup
~ backup_restore 2017-11-24_165120: restores the backup with id 2017-11-24_165120 and exits the plugin. You will have to relaunch the plugin after the restore is complete
~ database_sharing_active_connections_list: shows a list of the active Database Sharing connections
~ database_sharing_overwrite_local_data_with_remote: overwrites the local database with the remote database (warning there is no coming back, you'll lose all changes that were not saved). This can be useful to resynch plugins without restarting it. Use only as last resort
~ refresh: reinitializes session and connections (warning, if you do this during a race, all players will be reloaded and the session stats will be gone)
~ save: saves all the data in memory to files
~ exit: quits and saves the stats
---------------------------------------------
Server Admin Commands
~ admin_next_session: skips to next session (e.g. qualify->race)
~ admin_restart_session: restart the current session (e.g. restarts the race)
~ admin_send_command /ballast 0 100: sends the "/ballast 0 100" command to the Assetto Corsa server just like if you typed it in the chat
~ admin_say hello: broadcast "hello" to all players
~ rolling_start_toggle: toggles the rolling start flag for the next races (doesn't apply to the current session if it's already started)
~ virtual_safety_car_deploy 60: deploys the Virtual Safety Car for 60 seconds (only works at race).
~ player_list: gives a list of the online players (car_id:name:guid)
~ player_name 0: returns the player name associated with the slot number 0
~ player_parking_permit_toggle 0: allows/disallows the player in slot 0 to park everywhere on the track (e.g. for track recording sessions)
~ player_give_drive_through 0|1: gives a drive through to be served within 1 lap to the player associated with the slot number 0
~ player_cancel_drive_through 0: cancels the drive through penalty for the player associated with the slot number 0
~ player_drive_through_list: lists all the drive-through penalties that haven't been cleared yet
~ player_kick 0: kicks the player associated with the slot number 0
~ player_temporary_ban 0|60: bans the player in slot number 0 for 60 minutes
~ player_temporary_ban_guid 12345678901234567|60: bans the player with GUID 12345678901234567 for 60 minutes
~ player_ban_list: lists all the banned players
~ player_unban 12345678901234567: unbans the player with GUID 12345678901234567
~ reserved_slots_list: shows a list of the reserved slots
~ reserved_slots_add 12345678901234567: adds a reserved slot for steam GUID 12345678901234567
~ reserved_slots_remove 1: removes the reserved slots that has id = 1 in the output of the reserved_slots_list command
~ reserved_slots_announce: announces the reserved slots list to the Kissmyrank Master server (announcement is automatic so this command is not really needed but you can force the announcement to troubleshoot problems without restarting the plugin)
---------------------------------------------
Stats Management Commands
~ driver_get_guid Rockfeller: shows the GUID of "Rockfeller" (case sensitive)
~ driver_reset_money 12345678901234567: resets the money for Steam GUID 12345678901234567
~ driver_reset_times 12345678901234567: clears all the times for Steam GUID 12345678901234567
~ driver_reset_driving_stats 12345678901234567: clears the driving stats (driven km, collisions, wins, podiums, poles, fastest laps and driving infractions) for GUID 12345678901234567
~ driver_privacy_erase_personal_data_and_ban 12345678901234567: removes the driver with Steam GUID 12345678901234567 from the stats and bans him from the server (using a hash, since the GUID cannot be stored). This can be used if a driver decides to make use of his right to be forgotten. The reason for the ban is not to allow an abuser to clear the database from infractions just to abuse again. You can unban with the "driver_privacy_cancel_ban" command if a driver sends you his GUID.
~ driver_privacy_cancel_ban 12345678901234567: cancels the privacy ban for the driver with Steam GUID 12345678901234567 allowing him to join the server again
---------------------------------------------
Track Management Commands
~ track_get_length: returns the current track length in meters
~ track_set_length 5422: sets the current track length to 5422m
~ track_get_name: returns the name of the current track
~ track_set_name Monza: sets the current track human friendly name to Monza
~ pit_origin_remove 6: unsets the pit origin for slot id 6. This can help when for whatever reason the pit origin is not correct. Kissmyrank will then rebuild the pit origin in time (it might require a few sessions).
~ tracks_list: return a list of all the tracks defined in tracks.json
~ tracks_export monza_|ks_silverstone_national|mugello_|imola_: exports the selected tracks to a JSON file in the "export" folder
~ tracks_import tracks_to_import.json: imports the "tracks_to_import.json" file from the "import" folder to the tracks database (existing tracks will be overwitten, you should run "backup_create" before importing just to be sure)
---------------------------------------------
Track Rotation Commands
~ track_rotation_next_track: switches to the next track in the server rotation
~ track_rotation_list: shows a list of all the tracks in the rotation in the id|track|config|races format
~ track_rotation_current_track: shows the current track in the rotation
~ track_rotation_rotate_to 0: rotates to the track with id 0
~ track_rotation_vote_reset: cancels the current track rotation vote
~ track_rotation_get_races: shows the amount of races set for the current track in the rotation
~ track_rotation_set_races 10: sets to 10 the amount of races for the current track in the rotation
~ track_rotation_add vallelunga|extended_circuit|3|keep|{"PRACTICE": "remove", "QUALIFY": {"TIME": 10}, "RACE": {"LAPS": 10}}: adds {track: "vallelunga", config: "extended_circuit", "races": 3, entry_list_ini_path: "keep", ""ini_options": {"PRACTICE": "remove", "QUALIFY": {"TIME": 10}, "RACE": {"LAPS": 10}}} to the track list
~ track_rotation_edit 1|vallelunga|extended_circuit|3|keep|{"PRACTICE": "remove", "QUALIFY": {"TIME": 10}, "RACE": {"LAPS": 10}}: sets track 1 to {track: "vallelunga", config: "extended_circuit", "races": 3, entry_list_ini_path: "keep", ""ini_options": {"PRACTICE": "remove", "QUALIFY": {"TIME": 10}, "RACE": {"LAPS": 10}}}
~ track_rotation_remove 0: removes the track with id 0 from the rotation
~ track_rotation_save: saves the current track list to the config.json making it permanent (required if you want the new track list to stay if you restart the plugin)
---------------------------------------------
Cut Lines Commands
~ cut_line_list: shows a list of the cut_lines defined for the current track
~ cut_line_remove 1: removes the cut line that has id 1 in the output of the cut_line_list_command
~ cut_line_edit 1|pit entry speed limit line|80|0|0|0: updates the cut_line with id 1 in the cut_line_list with name=pit entry speed limit line, max_speed_kmh=80, outlap_only = 0, qualify_only= 0,race_only=0
~ cut_line_drawer_begin: starts a new cut_line sketch
~ cut_line_drawer_set_first_point 6: sets the first point of the cut line sketch on the current position of the car in the slot 6 (use player_list to get a list of the players slots)
~ cut_line_drawer_set_second_point 6: sets the second point of the cut line sketch on the current position of the car in the slot 6 (use player_list to get a list of the players slots)
~ cut_line_drawer_set_name pit entry speed limit line: set the name of the cut line sketch to pit entry
~ cut_line_drawer_set_max_speed 80: sets the max speed of the cut line sketch to 80km/h
~ cut_line_drawer_toggle_outlap_only: toggles the outlap only flag for the cut line sketch
~ cut_line_drawer_toggle_qualify_only: toggles the qualify only flag for the cut line sketch
~ cut_line_drawer_toggle_race_only: toggles the race only flag for the cut line sketch
~ cut_line_drawer_save: saves the current sketch to a permanent cut line
---------------------------------------------
Track Boundary
~ track_boundary_set_left 6: starts recording the left track boundary (please make sure you park your car before the start line before you launch the command)
~ track_boundary_set_right 6: starts recording the right track boundary (please make sure you park your car before the start line before you launch the command)
~ track_boundary_set_offset 1.0: sets the rendering offset of the track border to 1.0. This is not needed for regular tracks (which already default to 1). Use something around -1.0 for a wider rendering of street circuits where you cannot drive the capture outside the track)
~ track_boundary_clear_left: clears all the left track boundary data
~ track_boundary_clear_right: clears all the right track boundary data
---------------------------------------------
Track Boundary Exclusions/Inclusions
~ track_boundary_exclude_left_begin 6: starts recording of the left track boundary exclusion (please make sure you park your car before the beginning of area, then drive to the end of the exclusion where you should launch the track_boundary_exclude_left_end command)
~ track_boundary_exclude_right_begin 6: starts recording of the right track boundary exclusion (please make sure you park your car before the beginning of area, then drive to the end of the exclusion where you should launch the track_boundary_exclude_right_end command)
~ track_boundary_exclude_left_end 6: ends recording the left track boundary exclusion
~ track_boundary_exclude_right_end 6: ends recording the right track boundary exclusion
~ track_boundary_include_left_begin 6: starts recording of the left track boundary inclusion (please make sure you park your car before the beginning of area, then drive to the end of the inclusion where you should launch the track_boundary_include_left_end command)
~ track_boundary_include_right_begin 6: starts recording of the right track boundary inclusion (please make sure you park your car before the beginning of area, then drive to the end of the inclusion where you should launch the track_boundary_include_right_end command)
~ track_boundary_include_left_end 6: ends recording the left track boundary inclusion
~ track_boundary_include_right_end 6: ends recording the right track boundary inclusion
~ track_boundary_all_track_exclude_left: excludes the whole left track boundary
~ track_boundary_all_track_exclude_right: excludes the whole right track boundary
~ track_boundary_all_track_include_left: includes the whole left track boundary
~ track_boundary_all_track_include_right: includes the whole right track boundary
---------------------------------------------
Pit Boundary
~ pit_boundary_set_left_begin 6: starts recording the left pit boundary (please make sure you park your car before the beginning of the left pit boundary then slowly drive ahead along the border to the end of the pits where you should launch the pit_boundary_set_left_end command)
~ pit_boundary_set_right_begin 6: starts recording the right pit boundary (please make sure you park your car before the beginning of the right pit boundary then slowly drive ahead along the border to the end of the pits where you should launch the pit_boundary_set_right_end command)
~ pit_boundary_set_left_end 6: ends recording the left pit boundary
~ pit_boundary_set_ right_end 6: ends recording the right pit boundary
~ pit_boundary_clear_left: clears the left pit boundary data for the current track
~ pit_boundary_clear_right: clears the right pit boundary data for the current track
---------------------------------------------
Accessory Boundary
~ accessory_boundary_set_left_begin 6|Pit Entry Junction: starts recording the left Pit Entry Junction boundary (please make sure you park your car before the beginning of the left boundary of the desired area then slowly drive ahead along the border to the end of the area where you should launch the accessory_boundary_set_left_end command)
~ accessory_boundary_set_right_begin 6|Pit Entry Junction: starts recording the right Pit Entry Junction boundary (please make sure you park your car before the beginning of the right boundary of the desired area then slowly drive ahead along the border to the end of the area where you should launch the accessory_boundary_set_right_end command)
~ accessory_boundary_set_left_end 6: ends recording of the left Accessory Boundary area started by the car in slot 6
~ accessory_boundary_set_ right_end 6: ends recording of the right Accessory Boundary area started by the car in slot 6
~ accessory_boundary_clear_left Pit Entry Junction: clears the left Pit Entry Junction boundary data for the current track
~ accessory_boundary_clear_right Pit Entry Junction: clears the right Pit Entry Junction boundary data for the current track
--------------------------------------------
Cut Lines
The Cut Lines Feature allows you to define lines on the track which can be used to integrate the existing track boundaries (e.g. pit exit lines, pit entry speed limit, other critical cut areas that cannot be covered by boundaries etc.).
These lines can be used:
- to give penalty to players that cross the line
- to set a speed limit in a certain area of the track
- to prevent cutting in certain areas
Each cut line has the following properties:
- a name (pit entry speed limit line, pit exit line, your custom line)
- a speed limit over which to apply the penalty
- the coordinates of the first point
- the coordinates of the second point
- a outlap only flag (e.g if the cut line should be applied only if the player is in the outlap)
- a qualify only flag (e.g. if the cut line should be applied only during the qualify session)
- a race only flag (e.g if the cut line should be applied only during the race session)
You can define a cut line using your car as a reference. Here is how you do it:
Scenario 1: Pit exit line ( pictures can be found here: http://www.racedepartment.com/threads/kissmyrank-local-assetto-corsa-server-plugin.142199/page-6#post-2640347 )
1) Use the player_list command to get the slot id of the car that you wish to use to define the line (let's assume 6 for the purpose of this guide)
2) Start the cut line sketch by writing in the console the "cut_line_drawer_begin" command
3) Set the line name with "cut_line_drawer_set_name pit exit line$1" (most pit exit lines are not straight so you have to define it as a multi line, appending $1, $2, $3 to the line name is the way to tell the plugin that they are all part of the same line)
4) Set the max speed with "cut_line_drawer_set_max_speed 0" (the 0 tells the plugin that crossing the pit exit line at any speed greater than 0 will give a penalty which is exactly what we want)
5) Enable the outlap only flag with "cut_line_drawer_toggle_outlap_only" (this applies the penalty only to those that are in the outlap)
6) Drive your car to the start of the pit exit line segment that you wish to define. Place it exactly where the line begins.
7) Set the first point of the line with the "cut_line_drawer_set_first_point 6" command (where 6 is your car slot id as determined on point 1)
8) Drive your car to the end of the pit exit line segment that you wish to define
9) Set the second point of the line with the "cut_line_drawer_set_second_point 6"
10) Save the line with the "cut_line_drawer_save"
11) Repeat points 2-11 to define other segments of the pit exit line as needed (e.g. pit exit line$2, pit exit line$3) and so on.
Scenario 2: Pit entry speed limit line (for pit lane speeding)
1) Use the player_list command to get the slot id of the car that you wish to use to define the line (let's assume 6 for the purpose of this guide)
2) Start the cut line sketch by writing in the console the "cut_line_drawer_begin" command
3) Set the line name with "cut_line_drawer_set_name pit entry speed limit line" (no need for $ this time as this is going to be a single line)
4) Set the max speed with "cut_line_drawer_set_max_speed 80" (the 80 tells the plugin that crossing the pit entry speed limit line at any speed greater than 80 km/h will give a penalty which is exactly what we want)
5) Drive your car to the left end of the pit entry speed limit line. Place it as much to the left as possible.
6) Set the first point of the line with the "cut_line_drawer_set_first_point 6" command (where 6 is your car slot id as determined on point 1)
7) Drive your car to the right end of the pit entry speed limit line segment that you wish to define
8) Set the second point of the line with the "cut_line_drawer_set_second_point 6"
9) Save the line with the "cut_line_drawer_save"
Scenario 3: Your custom cut line (for the sake of this tutorial let's define a qualify only cut for the "Prima Variante" at Monza)
1) Use the player_list command to get the slot id of the car that you wish to use to define the line (let's assume 6 for the purpose of this guide)
2) Start the cut line sketch by writing in the console the "cut_line_drawer_begin" command
3) Set the line name with "cut_line_drawer_set_name prima variante$1" ($1 is only needed if you need it to be multi-line)
4) Set the max speed with "cut_line_drawer_set_max_speed 120" (people cutting this line at more than 120km/h will get a penalty)
5) Optional (if you wish the penalty to only apply in qualify or in the race use the "cut_line_drawer_toggle_qualify_only" or the "cut_line_drawer_toggle_race_only" command
6) Drive your car to the first point of the line that you wish to define (for the "Prima Variante" we could for example cover track re-entry on the part that leads to Biassono to check track re-entry speed)
7) Set the first point of the line with the "cut_line_drawer_set_first_point 6" command (where 6 is your car slot id as determined on point 1)
8) Drive your car to the end of the segment that you wish to define
9) Set the second point of the line with the "cut_line_drawer_set_second_point 6"
10) Save the line with the "cut_line_drawer_save"
11) Repeat points 2-11 to define other segments as needed (e.g. prima variante$2, prima variante$3) and so on.
You can list the cut lines for the current track with the cut_line_list command.
After you defined a cut line you can edit some of its settings with the cut_line_edit command.
Once defined you can save your work by typing save in the console.
Cut lines are effective as soon as you define them. You can disable the feature altogether by typing config_set cut_lines_enabled|0 and enable them back with config_set cut_lines_enabled|1.
The default tracks.json contains only the cut lines that I defined for some of the default tracks at development time. Some tracks might not have any cut line defined so, if you need them, you'll have to define them yourself.
If you have defined reliable cut lines, feel free to share the tracks.json file with me so that I can update the main package and share appropriate cut lines to new users of the Kissmyrank plugin.
--------------------------------------------
Track boundaries
Track boundaries are the track limits used to validate times, to prevent track cutting, to evaluate the hotlap/lapping status and to display the track in Race Control Replays.
Recording the track boundary is pretty straightforward:
0) Important: if you never did it before, please check and set the current track length in meters with the track_get_length and track_set_length commands.
1) Clear the old track boundary (if needed) with the "track_boundary_clear_left" and "track_boundary_clear_right" Kissmyrank Console commands.
2) Exit pits, drive your outlap and stop just before the start/finish line. Park it left, just outside the track.
3) Type player_list to get your slot number (6 for the sake of this example)
4) Type "track_boundary_set_left 6" and then slowly drive the full track along the boundary (use your car as reference and drive it the farthest that should be considered legal)
5) Once you completed the lap, you'll receive the Track Boundary Saved notification.
6) Repeat for the right track boundary.
7) Check the Track Boundary Exclusions section in order to learn how to exclude pit entry and pit exit.
Make sure you do not include pits in the capture (those need to be defined separately using the pit boundary commands).
Points recorded at a later time override the points taken before, so if you drive over a point again you can fix mistakes. However it is better to drive the full track boundary without repetitions.
Don't forget to run the save command when you're done (this will prevent data loss if you accidentally kill the plugin without running the proper exit command).
--------------------------------------------
Track Exclusions/Inclusions
These are used to define places where a driver can cross the boundary without getting penalties (e.g. pit entry, pit exit, straights, other areas where cutting gives no advantage etc.).
Recording exclusions is pretty straightforward:
0) Record the Track Boundaries first.
1) Drive to the start of the area that you wish to exclude
2) Type player_list to get your slot number (6 for the sake of this example)
3) Type "track_boundary_exclude_left_begin 6" and drive to the end
4) Once you reached the end of the junction stop the car and run the "track_boundary_exclude_left_end 6" command.
5) Repeat points 3-4 for other areas (for the right boundary just replace "left" with "right"). You can also reinclude an excluded area with the track_boundary_include_left_begin and track_boundary_include_right_begin commands etc.
Please note that although no penalties will be issued, laptimes will be still invalidated on boundary crossing regardless of inclusion and exclusion (times with all four wheels outside the white lines are not valid track records).
Don't forget to run the save command when you're done (this will prevent data loss if you accidentally kill the plugin without running the proper exit command).
--------------------------------------------
Pit boundaries
The Pit Boundaries define the Pit Area which is used for the Drive Through Penalty as well as outlap status detection and track drawing.
Recording the pit boundary is pretty straightforward:
0) Record the Track Boundaries first.
1) Clear the old pit boundary (if needed) with the "pit_boundary_clear_left" and "pit_boundary_clear_right" Kissmyrank Console commands.
2) Drive to the start of the pits and position the car on the left side.
3) Type player_list to get your slot number (6 for the sake of this example)
4) Type "pit_boundary_set_left_begin 6" and then slowly drive (drive always in the forward track direction, never reverse) the full pit along the boundary (drive as close as you can to the internal boundary)
5) Once you reached the end of the pit boundary stop the car and run the "pit_boundary_set_left_end 6" command.
6) Repeat 2-5 for the right pit boundary.
Assetto Corsa uses auto speed limiter. Stop the capture with the front of the car before the point where the spit limiter goes off or Drive-Through will be aborted if one has the foot on the gas when he reaches the line.
Make sure you include the full pits in the capture. Only capture the pit area (e.g. the area where the speed is limited to 80km/h). For road junctions please see Accessory Boundaries.
Don't forget to run the save command when you're done (this will prevent data loss if you accidentally kill the plugin without running the proper exit command).
--------------------------------------------
Accessory boundaries
Accessory area are only meant to give completeness to the track. They're not parsed for cuts and pit area detection but are shown on the map.
You can figure them as a drawing facility that helps you to complete the track (e.g. when the pit area is not connected to the track you can use this to complete the map).
Recording the accessory boundary is pretty straightforward. Let's make an example for the "Pit Entry Junction" (e.g. the part of asphalt that connects the track with the end of the pit area).
0) Decide a name for your area (names can be whatever you want and will be used in the Web Track Editor). In our case our name is "Pit Entry Junction";
1) Clear the old pit boundary (if needed) with the "accessory_boundary_clear_left Pit Entry Junction" and "accessory_boundary_clear_right Pit Entry Junction" Kissmyrank Console commands.
2) Drive to the start of the road junction and position the car on the left side.
3) Type player_list to get your slot number (6 for the sake of this example)
4) Type "accessory_boundary_set_left_begin 6|Pit Entry Junction" and then slowly drive along the boundary of the area
5) Once you reached the end of the junction stop the car and run the "accessory_boundary_set_left_end 6" command.
6) Repeat 2-5 for the right pit boundary.
Don't forget to run the save command when you're done (this will prevent data loss if you accidentally kill the plugin without running the proper exit command).
--------------------------------------------
Track Map
The track map is the place where you can visualize changes. Track map is available in the Race Control Web Panel via the event view button (you'll have to trigger an event to see it).
Please note that
- Race Control Event View requires both the right and left track boundaries and the pit area to be defined for a certain track (otherwise the event viewer has no reference and it will not load).
- If you update the track, changes should propagate to all browsers connected to Race Control in that very moment. If the browser is not connected you might need to clear the browser cache (as the track is cached to save some time).
--------------------------------------------
Web Track Editor
Once you capture the required areas of the track, you can then use the Web Track Editor to refine them.
The Web Track Editor is accessible via the event view:
1) Trigger an event (for example a cut)
2) Go to Race Control: http://yourip:web_port/race_control
3) Login as Race Director by typing your password (requires you to set the password in config.json first)
4) Click on the event and "View" it
5) Click Edit Track
6) You can now select the editing scope on the right and move points with your mouse
Left Mouse Click:
- select a point
- move the selected point to a new location
Left Mouse Drag:
- moves the view
Right Mouse Click:
- deselects the point
Middle Mouse Click
- toggles the include/exclude status (for track boundaries only)
7) Click save when you're done.
Note: excluded points appear in light blue.
Important: for efficiency and speed KMR maps points of the track into a lookup table. Use the track editor to make tiny adjustment perpendicular to the track (e.g. width or such) but avoid longitudinal movements as those might break the lookup table (thus resulting in cuts not being properly detected).
This doesn't apply to accessory area boundary points that can be moved as you see fit.
--------------------------------------------
Penalty Cost and Action Map
Config.json allows you to set a session based cost and an action for each infraction.
Supported sessions are:
- practice
- qualify
- race
- other
The available actions are:
- DT0 Drive-Through before the end of the current lap
- DT1 Drive-Through before the end of the next lap
- DT2 Drive-Through within 2 laps
- DT3 etc..
- K for kick
- TB30 Temporary ban for 30 minutes
- TB60 Temporary ban for 60 minutes
- TB61 etc.
Costs should be expressed in the usual format (1=1000€ if you use money).
You can map custom cut lines with "cut_line_your_custom_cut_line_name" (if you used multi line skip the part after and including "$")
--------------------------------------------
Assetto Corsa Chat to Kissmyrank Admin:
In order for this feature to work you must add your GUID to "ac_chat_admin_guid_list" and a valid password in "ac_chat_admin_password".
To login you need to type "/kmr login yourpassword" (don't forget the / or everyone will see your password).
After you manage to login you can run Kissmyrank Console Commands with "/kmr command" (e.g. "/kmr admin_say test").
--------------------------------------------
Player Chat Commands
~ kmr help: shows a list of commands
~ kmr language it: sets the language to "it" = Italian (type "kmr language") for a list of the available languages
~ kmr leaderboard: shows the fastest time on the server with the car that the player is driving
~ kmr level: shows the player level in the laptime challenge (if enabled)
~ kmr money: shows the amount of money that a player has
~ kmr best: shows the driver personal best with the car that the player is driving
~ kmr next_track: shows the next track in the server rotation (will only appear if the track rotation is active)
~ kmr rules: shows the server rules
~ kmr stats: shows the driver's driving stats
~ kmr toggle_notifications: toggles notifications while driving (rules will still apply but the driver will not be notified about damage, penalty and blue flags)
~ kmr vote_track: vote for track change (will only appear if the rotation is active and track_rotation_vote_min_percent is not 0)
~ kmr erase_my_personal_data_and_ban_myself: removes the player's personal data from the stats and prevents further access to the server (according to the right to be forgotten)
---------------------------------------------
Setup Notes
- Under Windows please make sure that Windows Firewall allows incoming connections to the plugin (they are required to communicate with the Assetto Corsa dedicated server).
- Drivers' Account balance and other stats are saved to rank.json (it will be created the first time stats needs to be saved). Please don't edit the file manually but rather use the provided commands.
- If you know how to, feel free to edit and customize the index.html template but be careful not to break its operation. The donate button is for those that want to support all the work I do on the plugin. Feel free to remove it if it disturbs you.
- To change the Web Stats Page favicon just replace the favicon.ico file with yours.
- The plugin has a lot of options, but as with all things, be careful when changing the configuration values.
---------------------------------------------
Gameplay Notes
- Race Entry Fee was introduced to promote responsible behavior and to encourage drivers to finish the race. Basically a driver pays to enter a race session and can make up for that amount only by finishing the race and cleanly beating another driver. Finishing the race does indeed pay.
- Sponsor fee and the race entry fee contribute to the total competition prize that is distributed among drivers that finish the race. Sponsor will pay more for longer races so that prices will be higher depending on the length of the race.
- Damage cost goes with the square of the velocity just like in real life.
- Prizes are paid to all those that pay the entry fee (e.g. are present at the beginning of the race) and that are not lapped more than twice.
- The minimum driving standard is a tool designed to control the quality of the drivers that join the server. Basically if you set it to 110% of the fastest lap, drivers that (in the specified amount of valid laps) haven't been able to post a time that is within 110% of the fastest time set with the very same car will not be able to join the server. We can safely assume that if in 12 valid laps a member hasn't been able to post a valid time he's probably going to need a bit of practice before he joins your server again.
- The minimum driving standard is fully customizable. By default it only kicks in if more than 12 players are on the server but you can change it according to your wish (always on, always off). This setting is designed to make sure that the drivers' quality doesn't deteriorate as the server gets full while not killing the server population when the server is empty. Cars that were not able to set a decent time, can be given a second chance to rejoin the server over time. For more about this please check the configuration file.
- Laptime Challenge allows new drivers to get some money by beating the time challenge and motivates them to set times. Laptime Challenge is fully customizable (prizes, levels etc.) and can be turned off altogether by setting the laptime_challenge_base_prize to 0.
- If too many collisions occur during the first lap of the race the plugin will deploy the Virtual Safety Car for 90 seconds. With config entry 136 you can set how many seconds you would like the Virtual Safety Car to last. If you set this to 0, the plugin will use auto race restart instead.
- Automatic Race Restart allows you to automatically restart the race if too many collisions occur in the first lap. This makes sense as a dirty start is often a prelude for a worse race ending (with several angry lapped cars). Automatic Race Restart it's a good way to train drivers and teach them that dirty driving does not pay. All the money loss will stay between one restart and the other in order to make sure that whoever is causing damage will not do it for long. Automatic restart on first lap collision carnage can be tweaked in the options. See config.json for more (set "first_lap_max_collision_player average" to 0 to disable the feature altogether).
- On a regular racing day you're always driving to the pits. If you park the car, someone will have to come and tow it, unless your pit crew is near enough to push it. config.json "car_towing_cost" allows you to set how much a driver will pay in this case (e.g. going to pits via the menu from more than what your pit crew muscles allow). This is meant to prevent abuse of respawn and thus prevent sensible driving.
- You can prevent drivers with high collision rates from joining the server. To do this, you can set the max_collisions_per_100km to anything you want (set to 0 to disable the feature altogether). max_collision_per_100km_min_distance is the driven distance over which this setting will apply. You can also set max_collisions_per_100km_recharge_hours if you wish to give drivers a second chance in time (set to 0 if you don't want to give a second chance).
- You can prevent drivers from abusing the reverse gear by setting "reverse_gear_max_distance" and "reverse_gear_penalty_cost" config.json entries.
- You can use "collisions_minimum_damage_with_environment" and "collisions_minimum_damage_between_cars" to prevent small collisions from being logged.
- "max_infractions" and "max_collisions" allow you to set the max_amount of infractions per session.
- Track boundary and cut lines cuts will invalidate the laptime as well as make a driver lose his hotlap protection status. After the first boundary cut, the plugin will force a customizable 80km/h limit for subsequent track boundaries cuts in the same lap.
- When going off track, a customizable limit of 120km/h will be enforced for rejoin track if there are drivers nearby.
- Kissmyrank can compare times posted by the drivers against the clock of the machine where it's hosted in order to prevent the most blatant CPU clock manipulation abuses. Due to networking and processing delays the resolution is not too high but it should still allow to filter out the most severe exploits. This feature will only be effective on powerful servers that can handle lap completion packets with steady delays. Please keep in mind that a few false positives can occur on server hiccups and such. However this is a little price to pay for more trustable laderboards. This is still an experimental feature. Set config entry 133 and to 0 if you wish to disable it.
- You can enable/disable Rolling Start in the options. Positions are locked during the formation lap. The race starts when the leader crosses the line.
- The Virtual Safety Car locks race positions and imposes a speed limit to all drivers. It can be triggered with the "virtual_safety_car_deploy" command.
---------------------------------------------
Assetto Corsa Auth Notes
- The Kissmyrank Plugin supports blocking bad drivers before they join the server via the Assetto Corsa Server AUTH. The Plugin Auth Server requires proper AUTH_PLUGIN_ADDRESS setting in the Assetto Corsa server_cfg.ini so that the Assetto Corsa Server can communicate with it. The proper auth string for the Assetto Corsa server_cfg.ini is written in the Kissmyrank Console every time you launch the plugin.
- The Kissmyrank Plugin supports blocking bad drivers via third-party services using the AUTH relay feature (see config.json entry 16). If you wish to add a third-party auth (e.g. another Kissmyrank Server Plugin, Minorating, Stracker etc.) you can edit the config.json "web_auth_relay_to" list. You can set as many as relay-to addresses you wish and block drivers from multiple sources. Driver that are banned in any of the specified systems will not be allowed to join the server.
---------------------------------------------
UDP Relay Notes
- The UDP Relay Feature allows you to use other plugins by relaying information coming from the Assetto Corsa server in the following way: Assetto Corsa Saver <-> Kissmyrank Plugin <-> Other plugins. Once you "linked" the plugin by adding the third-party plugin "ip:port" to the "udp_relay_to" config.json entry, you need to configure the other plugin as if the Kissmyrank Plugin were the Assetto Corsa server.
- To use Minorating via the Kissmyrank UDP Relay you need to add the following lines to the Minorating config: <add key="ac_server_port" value="12000" /><add key="plugin_port" value="10006" /> where 12000 is the port number that you used for the Kissmyrank "ac_server_plugin_address_port" and 10006 is the port number to use after the semicolon in the "udp_relay_to" list (e.g. replace UDP_PLUGIN_ADDRESS_1 with 127.0.0.1:10006).
- To use Stracker via the Kissmyrank UDP Relay you can set sendPort=12000 (where 12000 is the port number that you used for Kissmyrank) and set rcvPort to a value of your choice like 14003. You can then use this value for the udp_relay_to list (e.g. if rcvPort=14003 replace UDP_PLUGIN_ADDRESS_2 with 127.0.0.1:14003)
---------------------------------------------
Ping Limit Notes
- The Ping Limit Feature allows you to check the drivers' connection and verify their connection stability. Use the "max_ping" value to set the upper limit and the "max_ping_deviation" to control the connection stability. Assetto Corsa network code can work quite well with high pings as long as they are stable, so I recommend not to use values that are too restrictive as this might reduce the population of your server.
---------------------------------------------
Track Rotation Notes
- The Track Rotation Feature requires that you fill the correct path settings in the config.json file. If the settings are not correct, the plugin will notify you that the track rotation is disabled (in this case you have to manually launch the server). You can specify how many races you want to happen before each rotation and if you wish the rotation to occur when drivers are on the server. When the race limit is reached, players will be booted and the server track will change by terminating and relaunching your server. You can also manually trigger the track rotation by using the "next_track" console command. Do not use the same track twice.
- When you use the Track Rotation feature the Kissmyrank Plugin will start the server using the specified executable. In this case, please do not start the server manually or the plugin will not work correctly. Also notice that when you close the plugin the server will also be closed so please wait for races to be over before you do that.
- The ini_options track rotation config entry defined for each track lets you change server_cfg.ini entries before the track rotates. You could for example change the server name, the grip, the server password, the qualify time, the amount of laps, the weather or anything that comes to your mind.
- The ini_options must include the entries that you wish to set for each server_cfg.ini section for that rotation. Let's say that you want to change the server name to "My Awesome Imola Server", the qualify time to 30 minutes, remove the practice session and set the start grip to 97% with a session grip transfer of 75%. Normally to do this you would open the file and change the NAME entry of the [SERVER] section, the TIME entry of the [QUALIFY] section, the SESSION_START and SESSION_TRANSFER of the [DYNAMIC_TRACK] as well as removing the [PRACTICE] section. In order to achieve this with Kissmyrank. you need to set ini_options: {"SERVER": {"NAME": "My Awesome Imola Server"}, "QUALIFY": {"TIME": 30}, "PRACTICE": "remote", "DYNAMIC_TRACK": {"SESSION_START": 97, "SESSION_TRANSFER": 75}} and that's it. Now when the track rotates to that track rotation entry, the server_cfg.ini will be updated with those values.
- ini_options stick between one rotation and another so the server name will remain "My Awesome Imola Server" until you change it again. If a session was removed and you wish to add it back, it's enough to specify the TIME (qualify and practice) or the LAPS (race) value.
- If you rotate to a track with a limited number of slots (e.g. Magione) please remember to use the ini_options to set MAX_CLIENTS according to your needs e.g. {"SERVER": {"MAX_CLIENTS": 9}}). Also keep in mind that ini_options stick between one track change and the other so you might need to add MAX_CLIENTS to the other tracks as well to revert the setting as needed.
- entry_list_ini_path, specified for each track, allows you to change the entry_list.ini when the track rotates (e.g. change cars, teams, ballast etc.). Files are copied over the Assetto Corsa default entry_list.ini (which means that you need to keep separate files in another location for all your desired configurations). You can use "keep" if you wish to keep the existing entry_list.ini between one rotation and the other (same as specifying to use the default path). If your new entry_list.ini changes the cars, you also need to use the ini_options setting SERVER=>CARS to update your server car list (e.g. "SERVER": {CARS: "ferrari_458_gt2;bmw_m3_gt2"}). Please notice that the Kissmyrank Multiplayer Launcher auto-rejoin will not work if the entry_list.ini is changed (if you change the car list, people cannot rejoin with their previous car).
- You can automate actions (e.g. launch a program, a script etc.) before and after the Assetto Corsa Server is launched using the "before_ac_server_start_run_path" and "after_ac_server_start_run_path" config.json entries. Please notice that if "before_ac_server_start_run_path" is set, Kissmyrank will wait for the specified program to terminate before launching the server. If your program doesn't terminate quickly, please use a shell script or the "after_ac_server_start_run_path" (which doesn't wait for the call) to launch it, not to delay the Assetto Corsa Server launch process.
- The json_verify command is your friend to see if your entry is valid. To visualize an entry you can visit: http://jsonparseronline.com/
- The kmr vote_track command allows players to vote for one of the tracks in the current rotation. Admins can reset the vote (before the track rotates) using the track_rotation_vote_reset console command. track_rotation_vote_min_votes can be used to set a minimum amount of votes required for the track change to start (useful if you don't want lonely players to be able to change the track). track_rotation_vote_min_percent allows you to set the % of players that have to cast a vote before the track change occurs. When a sufficient number of votes have been casted, the track will switch to the most voted one.
---------------------------------------------
Launcher Multiplayer Mod Notes
- The Kissmyrank Assetto Corsa Multiplayer Launcher Mod allows you to auto-reconnect on track change via the use of the Kissmyrank Master Server. It also allows you to join a full server as soon as a slot opens up ( demo: https://youtu.be/0RdEasAO-h4 , download: https://www.dropbox.com/sh/7lp4mobixpdx7x3/AABWelmzZlJPysxnRwJK-DL4a?dl=0 ).
- Reserved slots allow the VIP players whose GUID has been added to the config.json "reserved_slots_guid_list" to join the server even if it's full.
- The reserved slot feature requires the Kissmyrank Assetto Corsa Multiplayer Launcher v0.1b or greater. Keep in mind that this feature might kick players to make room for VIP players (it kicks drivers starting from the bottom of the leaderboard that is to say those who just joined or the ones with the worse performance). This is the only way for you to make it on your server if it's full. For this to work, you need to define the "reserved_slots_guid_list" and "reserved_slots_access_key" in the config.json and type the access key in the Kissmyrank Assetto Corsa Multiplayer Launcher Mod (the access key input box will appear near the server list ping and help buttons). If any of these is not set, the feature will be disabled for safety.
- "reserved_slots_boot_players_at_race" allows you to control if you want the Reserved Slot Feature to kick players during the race (if you set this to 0, VIP players that want to join during a race will have to wait for a slot to naturally open up or for the end of the session).
---------------------------------------------
Database Sharing Notes
- With the Local Database Sharing feature you can share the rank, tracks and leaderboard database between different instances of the plugin running on the same machine. To use this feature you just need to set "database_sharing_unique_name" to a unique name for each plugin and then set "database_sharing_local_group_port" in the config.json to the same value for all the instances that will be sharing the database (leave the other entries alone as those are only required for remote sharing). You can create separate groups by picking a different port for each group (e.g. 4567 for group 1, 4568 for group 2 and so on). "database_sharing_unique_name" will help you to identify plugins in the Kissmyrank Console Log so make sure you pick a different one for each instance.
- With the Remote Database Sharing feature you can connect instances that run on a different machines. For this you need to set "database_sharing_unique_name", "database_sharing_remote_listen_port", "database_sharing_remote_secret_key", "database_sharing_remote_connect_to_addresses" as described in the config.json. Remote database sharing is not as reliable as Local Sharing. Connection might drop and there might be lags. The plugin will try to recover whenever possible but better to use Local Database Sharing whenever it's possible.
- When using either Local or Remote Database Sharing, the plugin will use the database of the first member to start. When the databases are in sync, you can then turn off any group member and restart it at any time. The other plugins will keep on updating the shared database and send it to the offline member the next time that it starts.
- Let's say that you want to share the database between 3 plugins (A,B and C) and that you set database_sharing_unique_name to "plugin_a", "plugin_b", "plugin_c" respectively. Let's say that you can only connect A<->B and B<->C but you can't connect A with C directly. After properly setting all the other keys for (A<->B and B<->C), you then edit plugin_b config.json and set "database_sharing_relay_for_names" to ["plugin_a", "plugin_b"]. This will tell plugin_b to relay database updates to the other plugins allowing you to do A<->B<->C. Keep in mind that in this case if you take down B, you have to also take down A and C or the synchronization might not fully apply. This feature works for both local and remote connections as long as you set the unique name. This feature is to relay information to lonely plugins. Be careful not to create double links between plugins or you might get double updates.
- Pay attention to the red warning messages when using Database Sharing. They will notify if anything is wrong and help you prevent any problem. Use the database_sharing_active_connections_list command to get a list of the active connections at any time. The "database_sharing_overwrite_local_data_with_remote" command can be used to force a synchronization if it's lost. Keep in mind that any change that is not already on the remote database might get lost if you run this command.
---------------------------------------------
Web Admin Console
- The Web Admin Console allows you to access the Kissmyrank Console with the use of your Web Browser
- The Kissmyrank Web Admin Console is located at http://yourserverip/kissmyrank_admin (same port as the web stats).
- The password needs to be at least 12 characters long.
- To login type "login password" (e.g. "login yourcomplexpassword").
---------------------------------------------
General Notes
- Whenever you meet arrays in config.json (e.g. ["one","two","three"]) you can extend these config entries as much as you want by replicating the same syntax inside the squared brackets (e.g. ["one", "two", "three", "four", "five", "six"]). For example you can set as many UDP and AUTH relays as you want (the only limit being your system resources).
- This plugin makes a very rough estimate of the track length. I recommend you use the set_track_length command to update the length if it's not accurate.
- Pit origin database might require a little to build up. This might lead to a few towing cost anomalies during the first use of a new track.
- The proper way to quit (so that all the data is saved) is by typing "exit" in the console.
- The refresh command will make you lose any unsaved change. Type save first if you wish to save.
- The config_set command allows you to edit the config.json at runtime. You need to specify the argument in the config_id|value format where value is exactly what would appear in the config.json file for that config_id (e.g. config_set currency_symbol|"€" or config_set max_ping|300). Please notice that, for the value, double-quotes need to be present whenever they are present in the config.json as shown in the examples. On the contrary, the config_id never needs to be enclosed within double-quotes. The changes you make are permanently saved to config.json. In the backup folder you can find older copies of config.json (a backup is made whenever you start the plugin). Most values will apply immediately but some values might require a plugin restart to apply.
---------------------------------------------
Troubleshooting:
If editing config.json with your favorite editor makes it "broken" please check that you're editing and saving it in the UTF8 format.
Timeout errors are an indication of a communication problem with the Assetto Corsa server or that max_players is not matching the number of slots on your server. Please check your configuration.
If the plugin doesn't give you the track information when you start it then it's not able to communicate with the server. Just close it, fix the problem and then try again.
If you get the "In use" error it means that the plugin is already launched or that the port is used by another service.
Independently backup the plugin folder from time to time.
I suggest to always use the available console commands. Never edit the json files unless you know what you're doing. If you do a mistake stats might reset.
If you get any issue, try the default configuration values first and double-check the setup. If it was previously working you can also restore a backup with the "backup_restore" command.
If you're running Linux and the web server doesn't start, it's because processes without root privileges cannot bind ports below 1024. In this case you can use iptables to create a redirection using the command "sudo iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j REDIRECT --to-port 8080" where 8080 would be the plugin "web_stats_server_port".
If you're running Windows and the plugin gets stuck until a keypress, it might be because "Quick Edit Mode" is turned on. When you accidentally click or drag on the console text, Windows might pause the execution until you quit the selection mode with a right-click. You can disable "Quick Edit Mode" by right-clicking the top bar and selecting "Properties".
---------------------------------------------
Translation Help Needed:
It will greatly help if you can translate /language/en.json to your language and then send the translation to me.
Here is how to translate (we'll use "de" for the purpose of this example):
1) Copy /language/en.json to /language/de.json
2) Edit de.json with a text editor that supports "UTF-8"
3) Translate every sentence to German paying attention to keep the replacement patterns (e.g. %s %d %f etc.) in the same order as they appear in the original string
4) Save as "UTF-8"
5) Send the translated file to me over Race Department or the Assetto Corsa forum so that I can include it in the package.
---------------------------------------------
Notes about the "%s" "%d" etc. replacements that you find in strings:
These identifiers are placeholders for the values that the plugin will write so:
- they have to be there
- they must appear in the same order as in the original English string
Example:
Consider this string:
    The speed limit is %s and %s's speed is %s.
The plugin will replace the first occurrence of %s with the speed limit, the second with the driver's name and the third with the driver's speed.
Final result:
    The speed limit is 140km/h and Brioche's speed is 120km/h.
When you translate you need to make sure you respect the order.
So in Italian this needs to be translated to:
     Il limite di velocità è %s e la velocità di %s è %s.
Which will become:
    Il limite di velocità è 140km/h e la velocità di Brioche è 120km/h.
Finally if you encounter something like:
    %s%d%sspeed
You'll have to retain the existing pattern and translate it to:
    %s%d%svelocità
---------------------------------------------
App Link Notes:
The App Link allows your Kissmyrank server to send data directly to Assetto Corsa in-game apps without relying on the chat.
App Link documentation is available under /applink/doc/
App Link Demo App is available under /applink/demo/
---------------------------------------------
Download: https://www.dropbox.com/sh/7lp4mobixpdx7x3/AABWelmzZlJPysxnRwJK-DL4a?dl=0
---------------------------------------------
Changelog
v0.1 Fixed an issue with ranks not saving on exit. Updated configuration entries.
v0.1a New list_players command. Added console logging for pole and race winner.
v0.2 Switched to money for the sake of better realism. This better justifies both cars being penalized in a collision as they have to pay to repair the car. Collisions now cost 1000€ each. This opens many possibilities and could be used for other rating systems too.
v0.2a Race entry fee. Entering a race now costs money. Set to 0 to disable.
v0.2b Fixed a few minor things with rank auto-save, kick messages etc.. Changed default warned_car_grace cfg value.
v0.3 Increased default car update rate. Lapping and hotlapping protection is now more reliable. Protection area is now expressed in meters. Drivers now have to also pay for collisions with the environment. Collisions repair cost is now gauged against the relative velocity. Collision base cost for both environment and car collisions can be set in the config. You can now change the currency symbol and the thousands separator. Prizes are now related to the entry and sponsor fees. Added support for the practice session. Better race result calculation. Added more logging in the console. This is a major update, please make sure you use the latest config.json file.
v0.3a Fixed a silly issue with paths that would crash the plugin on start.
v0.3b Fixed an issue with auto-kick.
v0.4 Added Leaderboard (times are saved per car and per track). Added a Web Stats Server (http://yourserverip/) that allows everyone to access the Leaderboard. Default port is 80. You can change port by editing config.json. Added Chat commands: now players can request their stats, toggle notifications etc.. Type kmr help in game for a list of commands. Penalty cost can now be set in the config. Lapping and hotlapping cars are now going to be charged for damage on their car (this is more fair as they already get the protection and the offending car is fined with the additional penalty, thanks AJ Clarke for the feedback). Fixed an issue with auto-kick on join not working properly. Race prize is now also based on race length. Added fastest lap announcement in race. Added fastest lap prize (in race and overall). You can now see which car was driven by the player that took the pole or set the fastest lap. Added Server Minimum Driving Requirement Standard: this allows to filter out players that are not capable to set a time within x% (default 110%) of the fastest Leaderboard lap (with the same car) in a certain amount of valid laps. This feature is fully customizable: you can set it to only work when the server is getting full and control if players should be given a second chance over time. Set minimum_driving_standard to 0 to disable the feature altogether. Added new console commands (reload, save, get_track_length, set_track_length, get_track_name, set_track_name, get_money, reset_money) for controlling the plugin without restart. Better handling of track change, server name change and server restart (just type "save" and then "reload" if needed and the plugin will automatically parse the new server configuration). Many other improvements and fixes. This is a major update, replace all the files in the folder with the new ones (including config.json and tracks.json) and then edit the new configuration as you see fit.
v0.4a Fixed missing AC server name on the Web Stats Page.
v0.4b Added Recent Activity tab to the Web Stats. Laptime Challenge (gives reward to players as they get faster and level up). This is useful to motivate players to set times. Reward can be set in the options (set to 0 to disable the feature altogether). Fixed an issue with prizes not being assigned to drivers that disconnect immediately on race finish.
v0.4c Implemented support for the Assetto Corsa Auth. The Kissmyrank Plugin can now poll external auth servers via its auth relay feature (e.g. Minorating, Stracker, another Kissmyrank Plugin etc., see config.json for more). Fixed an issue with incorrect damage calculation. Added support for time based races. Fixed incorrect race prize calculation. config.json has changed. Please update the old file. Thanks to Bruno32600 for all the feedback so far.
v0.4d Fixed wrong AUTH_PLUGIN_ADDRESS tip on plugin start.
v0.4e Fixed car_id is not defined error. Added configuration options to control the race auto-restart depending on the first lap collision count (see config.json for more). config.json was updated. Please overwrite the old file.
v0.5 New UDP Relay Feature that allows to relay the information coming from the Assetto Corsa server to other UDP plugins. It works like AC Server <-> Kissmyrank Plugin <-> Other plugins (e.g Minorating, Stracker etc.). In order for this to work you need to set the other plugins as if the Kissmyrank plugin were the AC Server (have a look at the config for more). config.json was updated. Please overwrite the old file.
v0.5a Fixed multiple auto-restarts on first lap carnage.
v0.5b New Ping Limit: you can configure "max_ping" and "max_ping_deviation" limits, as well as the ping check interval (amount of time between two consecutive measurements). Added "race_min_players" value to the config. Collision chat notifications now include the name of the other driver. config.json was changed. Update accordingly and don't forget to configure the proper "ac_server_http_port" so that it matches your server_cfg.ini HTTP_PORT.
v0.5c Fixed car check when the car is not connected. Fixed UDP Relay not working properly. Other improvements and fixes. Thanks to IZI for helping with the tests.
v0.6 New Track rotation (see config for the options and the readme for more). If you use the Track Rotation feature, the Kissmyrank Plugin will launch the server (do not launch the server manually). Join queue and auto-rejoin on track rotation are available via the Kissmyrank Assetto Corsa Multiplayer Launcher Mod. config.json was updated. Added File Backup on start. config.json has changed. Please overwrite the old file and edit the configuration anew.
v0.6a Added track_rotation_max_players (set to 0 if you wish to only rotate the next time that the server is empty, 99 or any number greater than the number of slots to rotate at any time). warned_car_grace is now in expressed in seconds (update your config accordingly). Added session recovery if the new session packet gets lost (for qualify and time based races). Fixed refreshing loop. config.json was updated. Please update your config.
v0.6b Fixed player list not being reset on track rotation.
v0.6c New First Launch Setup Wizard to facilitate the first time setup. Other improvements and fixes.
v0.6d Fixed rotation doesn't work as expected when config is specified. Fixed unexpected server termination when track rotation is active. Optimized players connection handler. Added 900ms timeout on auth relay not to delay the join process too much. Other improvements and fixes.
v0.6e Improved configuration check for directories and files. Better handling of Assetto Corsa Server launch failures. Improved Setup Wizard input validation.
v0.6f New Startup Port Check (to prevent accidentally running the plugin twice or running the track rotation with an external instance of acServer already running). If config.json is broken you will now receive a note allowing you to fix the config before it's overwritten. Improved handling of the Assetto Corsa Server exit codes.
v0.6g Fixed an error with UDP Relay not starting due to recent changes. New track_list, current_track, track_rotate_to, track_get_races, track_set_races, add_track, edit_track, remove_track, save_track_list, config_set console commands. Added Startup Backup of config.json (since now you can permanently update the config at runtime, you might need a backup if you want to revert some edits).
v0.6h New Car Towing Cost. On a regular racing day, you're always driving to the pits. If you park the car, someone will have to come and tow it unless your pit crew is near enough to push it. If "car_towing_cost" is set and you go back to pits without driving, you'll have to pay the car towing fee (set "car_towing_cost" to 0 to disable). This feature should allow for better immersion for those who like to have it on their servers. Added configuration for the clean gain reward (previously it was hardcoded, set "race_sponsor_clean_gain_reward" to 0 to disable the feature altogether). Fixed setup wizard not behaving properly on the first answer. Private/public net range checks for the setup wizard if you wish to try to use the plugin remotely over the Internet. Other minor fixes. Changed the order of the default config entries for less confusion on future updates (this is the last time that the order should change, so I recommend to generate the config anew. It will be easier for you to update and maintain it in the future. If you already have a config and you don't want to create a new one, just add the new options 32, 33, 54 at the bottom of your current config.json. Please be sure that you add a comma after the last entry of your current config.json before you add the new lines).
0.7 New Cut Lines. You can now define cut lines on the track and give penalty to players that cross them (any speed or speed limit). Creating a cut line is easy. All you have to do is just parking your car on the two ends of the line and run Kissmyrank console commands. Each cut line is fully customizable meaning that you can assign a penalty, a max speed in km/h, outlap only, qualify only and race only flags (please check the readme for more). Special cut lines can be defined for pit entry speed limit line (aka pit lane speeding penalty) and pit exit line. You can disable line cutting detection using the "cut_lines_enabled" config.json entry if you don't want to use the feature. New Web Results (it shows a log of the last 30 sessions on the Web Stats page). You can decide how many sessions to keep. New Backup feature to automatically restore the backups in the backup folder. Better detection of corrupt files. New reserved slots feature. If the server is full, the Kissmyrank plugin will attempt to make room for the selected GUIDs (requires the Kissmyrank Multiplayer Launcher Mod v0.1b+). Improved: towing cost now depends on the distance. New: money penalty instead of kick for hotlapping/lapping protection (set the penalty cost to 0 if you wish to use the old kick system in this case). You can set different punishment for quali and race. Improved: reorganized all the commands. Improved: pit origin is now saved to tracks.json (the database will need a while to build up). New total collisions and driven distance are now logged per player and can be seen in the web stats. New commands to reset player stats and times if something goes wrong. Other improvement and fixes. This is a major update which will partly modify the json file structure. Backup your old folder before updating in case you need to recover. Clear your backup folder as the backup system has now changed. Do not overwrite your current tracks.json with the new one right away. Run the new plugin once and type "save" in the console. This will move the leaderboard from tracks.json to leaderboard.json. After that you can exit and overwrite tracks.json with the new one. Update config.json entries from 54 to 61 (these are new and are required to run the new version of the plugin).
v0.7a Disabled memory monitor by default (since it requires libc6 2.14+ that is not available in some older versions of Linux) and added entry 62 to config.json to turn the feature on and off.
v0.7b Fixed Web Stats driver list not showing total collisions if the collision number is zero. Changed collisions per km to collisions per 100km for better readability.
v0.7c Added backup_list, backup_create and backup_restore commands.
v0.7d Fixed driven distance displaying with the wrong amount of decimal digits in the Web Stats. Added Best Lap to the Web Stats race results. Improved Web Stats results visualization when no valid lap was recorded. Fixed Web Stats showing the wrong pole lap in case of cuts. Added live money check for the new money based lapping/hotlapping penalties (so that wreckers get kicked immediately when they go below the min money value that you set in the config). Improved the calculation of the distance driven by a certain driver.
v0.8 New Database Sharing: you can now share the rank, tracks and leaderboard database between different instances of the Kissmyrank plugin that are running on the same machine and/or remotely. If the Kissmyrank instances run locally, you just need to set "database_sharing_unique_name" to a unique name for each plugin and then set "database_sharing_local_group_port" in the config.json to the same value for all the instances that will be sharing the database (no other entries are required as all the other settings are for remote). You can create different local groups by picking a different port for each group (e.g. 4567 for group 1, 4568 for group 2 and so on). If the instances run on a different machine, you need to set "database_sharing_remote_listen_port", "database_sharing_remote_secret_key" and "database_sharing_remote_connect_to_addresses" as described in the config.json documentation. New Track Rotation ini_options. You can now change server_cfg.ini entries when rotating to a certain track (e.g. change server name for each track, set sessions, grip, weather etc.). See the readme for more. New: console command autocompletion, yay, no more typing errors when looking for a command. New "help command_name" console command to get help about a certain command. New: pagination for ranks as the list can get very long. Improved: cut_line_drawer now shows you which commands are left to finalize the cut line sketch. Fixed reserved slots handler kicking players that have a reserved slot to make room for other players with reserved slots (ouch). Other improvements and fixes. tracks.json contains more up to date track info so you might want to update that too (leaderboard was moved in 0.7 to a separate file so if you run this version and you haven't defined new cut lines, you can overwrite tracks.json no problem). New entries in config.json are 63-69. Entry 22 has changed. Please update your config accordingly.
v0.8a New Kissmyrank Web Admin Console: you can now manage the Kissmyrank plugin and the Assetto Corsa server from the Web Browser via the Kissmyrank Web Admin Console ( http://yourserverip/kissmyrank_admin ). This feature will be disabled unless you set the "web_admin_console_password" config.json entry to a password of at least 12 characters. New admin_send_command: you can now send commands to the Assetto Corsa Server just like if you were typing in the game chat (e.g /ban_id, /ballast etc.). Added config entry 70. Please update your config.json accordingly.
v0.8b New "on_ac_server_start_run_path" config.json option that allows you to run a program or a shell script when the Assetto Corsa Server starts (you can use it to restart other plugins or perform other tasks when the Assetto Corsa Server rotates the track etc.). Added config entry 71. Update your config.json accordingly.
v0.8c New max_collisions_per_100km setting: you can now prevent drivers with high collision rate from joining the server (set to 0 to disable the feature altogether). You can set the driven distance over which this setting should apply (max_collision_per_100km_min_distance) and if there should be a recharge period (in order to allow players with high collision rates to join the server again after a certain amount of time). Added reserved_slots_boot_players_at_race config.json entry if you wish to prevent the Reserved Slot Feature from kicking drivers during the race (keep in mind that kicking happens from the very bottom of the grid and that if you set this to 0 VIP players will have to wait for a slot to naturally open up or for the end of the race). Added driver search in the Web Stats drivers page (you can search both by name and GUID). Added sorting to all tables and fixed format mismatch for decimal separators. New player_temporary_ban, player_temporary_ban_guid, player_ban_list, player_unban commands to allow you to temporarily block a driver (this is intended for short lived bans and it resets when you restart the plugin). Added option to vote for next track (kmr vote_track chat command). You can choose how many votes are needed to trigger a track change (percent and min). See config.json for more. Set track_rotation_vote_min_percent to 0 to disable the feature altogether. Added config.json entries 72-77. Please update your config.json accordingly.
v0.8d Added config.json option to send one or more custom chat driver welcome messages when a driver connects. New config entry 78. Please update your config.json accordingly.
v0.8e Added Minorating step by step configuration support to the First Launch Setup Wizard for an easier setup of the UDP and AUTH relays for those that wish to use it. Added more checks for the Assetto Corsa server executable path in the First Launch Setup Wizard for Windows users (thanks to berggeit from RD for the tip).
v0.8f New Reverse Gear Penalty: you can now set the maximum distance a driver can drive in reverse and the penalty that he will get for the abuse. New "entry_list_ini_path" track list option that allows you to change Assetto Corsa Server entry_list.ini when the track rotates (if you change the entry list, Kissmyrank auto-rejoin will be disabled as drivers will not be able to rejoin with their previous car). New "collision_minimum_damage_with_environment" and "collision_minimum_damage_with_cars" if you don't wish to log small collisions (set to 0 to log all collisions). New "before_ac_server_start_run_path" that allows you to run and wait for the execution of a script before the Assetto Corsa Server is launched (e.g. track rotation). Added driver's stats to the Kissmyrank Welcome Message (driven distance and collisions). New "kmr stats" chat command. Added favicon.ico support to the Web Stats page (just replace the file with yours to customize). Fixed track not rotating when the track id is 0. Renamed "kmr mybest" chat command to "kmr best". Renamed "on_ac_server_start_run_path" to "after_ac_server_start_run_path". Other improvements and fixes. Changed entry 22 and 71. New config entries 79-83. Please update your config.json accordingly.
v0.9 New Heuristic Driving Line Analyzer: Kissmyrank can now check and learn from drivers' lines. The collected data is then used to evaluate drivers' behavior on track (like getting an unfair advantage by cutting the track) and to improve some of the plugin mechanics (hotlap status, lapping etc.). This feature might require some disk space (set "heuristic_driving_line_analyzer" config.json entry to 0 to disable the feature altogether). For further information, please check the readme.txt. New track cut and heuristic track cut kick penalties: you can set a maximum number of cuts a driver is allowed during a session (see the "max_track_cuts" and "heuristic_max_track_cuts" options). Bonus: Heuristic Driving Line Analyzer cuts are detected in real time and you can force a stop and go before the end of the lap when the limit is reached. Drivers can clear their penalties and avoid the kick by taking a stop and go penalty (see the "track_cuts_clear_on_stop_and_go" and "heuristic_track_cuts_clear_on_stop_and_go" options). Added "web_stats_drivers_per_page" config.json entry to control the Web Stats Drivers List pagination. Disabled database sharing update parse/relay console log messages (they will clutter the log if there are many updates). Other improvements and fixes. New config entries 84-104 are required to run. Please update your config.json accordingly.
v0.9a Refined the Heuristic Driving Line Strip model. Fixed: some Heuristic Driving Line Analyzer bugs. New gZip compression for the JSON files backup process (to save disk space). For a cleaner approach, the "backup_restore" and "backup_list" commands now only support the new gZip format. Since there are important fixes for the Heuristic Driving Line Analyzer, you should run the "heuristic_all_tracks_all_data_clear" command after updating so that the Heuristic database can be rebuilt. Also it wouldn't hurt to clean up your backup folder (you can move old files to another folder in case you need them at a later time).
v0.9b Temporarily disabled the Heuristic Driving Line Analyzer in the default config as I need to study the collected data and perform further optimizations first (you can still enable it if you want). If you see any issue when you're testing it, I recommend setting heuristic_driving_line_analyzer to 0 in the options and sending the tracks.json file to me. I can learn a lot from the data in it. Fixed other minor issues. Changed default update interval to 200ms (for better reverse gear detection). Updated default tracks.json with new data. If you're already running the plugin, you can disable the Heuristic Driving Line Analyzer by typing "config_set heuristic_driving_line_analyzer|0".
v1.0 New: Live Race Control. Race Officials, Teams and Drivers can review race happenings live with a Web Browser without the need of a replay. Live Race Control is accessible over the integrated Kissmyrank Web Stats Server (http://yourserverip/race_control). Whenever an event occurs during one of the sessions, it gets reported live to Race Control where race directors can login and review the driving lines and confirm/override the automated penalty system fines (under investigation and official penalty notifications will be broadcasted to the chat if the event was in the current session). New: Track boundaries: you can now define track boundaries by driving your car along the limits of the track. New: tracks.json now includes boundaries and some cut_lines for many tracks. Please replace the old tracks.json which might contain obsolete data and then add your own custom cut lines as needed. You can also redefine the boundaries as you wish using the provided commands. Improved: track boundaries and cut_lines are now part of the Live Cut Detection System which works with the integrated "Stop and Go to Clear" feature. Scrapped: Heuristic has been totally removed from the plugin (due to limited sampling rate and error propagation it could not work properly). Added: "clean_lap_reward" config.json entry to set a tiny reward for players that complete a valid lap without cutting the track (useful for practice servers). Added: RACE_EXTRA_LAP support. config.json entries starting from 86 are all new. Please remove the old entries and then add the new ones. This is a major update. I recommend to backup the old plugin folder and then clear your log and backup folders.
v1.0a Fixed: invalid car projection when magnifying factors don't match. Fixed: wrong penalty when crossing outlap only cut lines on race start. Fixed: missing time_based_race_extra_lap detection when the track hasn't yet rotated. Fixed: config_get and config_set commands failing when the current value is null.
v1.0b Fixed: cleanup of old race control events triggering the "cannot convert" error. Added "ac_server_restart_if_inactive_for_minutes" config.json entry to restart the Assetto Corsa server if no activity occurs for more than the specified amount of time (only works when the track rotation is enabled). Improved: increased collision time to prevent the same collision from being logged twice. New config.json entry 102. Please add it to your config.json.
v1.0c Fixed: Race Control events piling up due to broken cleanup (possibly leading to a crash on busy servers). Added: ability to filter Race Control events by session. Fixed: Race Control filters not working properly on some occasions. Improved: session type and start time are now shown in the Race Control Event Viewer. Improved: the number of session cuts for a driver is now included in the Race Control event description. Improved: extended track boundary cut detection area for a more precise detection. Important: delete ~temp.json as it contains obsolete incompatible data. New config.json entries 103-104. Please update your config.json accordingly.
v1.0d Fixed: error cw1 spam. Improved: Race control now shows recent events first. Added: option to reverse sort (if you wish to get back to the older sorting). Added: Debug info for two errors that I am trying to debug (please send the log to me if you see debug information in the console).
v1.0e Fixed: saving big JSON files causes delays during the session switch process. Fixed: saving big JSON files can cause high memory consumption (potentially leading to a crash on low specs systems). Fixed: circular reference error popping up when quickly refreshing the online Web Stats. Please note that quitting the plugin might take slightly longer now, as the database write process is optimized to use a limited amount of resources (this will keep more resources free for the other processes running on your server).
v1.0f New: Wins, Podiums, Poles and Fastest Laps counters are now part of the Kissmyrank statistics. Fixed: Reserved Slots handler not freeing a slot when a VIP connects to a full server. Improved: Web Stats Results now show the cut count, the collision count and the tyre change history for each driver that completed the race. Fixed: Web Stats online list sorts positions as text instead of number. Added: Kissmyrank version information is now shown in the Web Stats Pages footer. Improved: the plugin will skip saving big JSON files on new session if players are on the server in order to save CPU for multi-server setups. Added: "race_control_log_overtakes" configuration entry to disable overtake logging (as overtakes provide redundant information that doesn't need to be analyzed for the most part). Added: "web_stats_results_show_lap_log" config entry to hide the Lap log from the Web Stats Results viewer as it contains unnecessary redundant information. config.json entries 105-106 are new. Please update your config.json accordingly.
v1.0g Added: Driving Infractions counter (includes cut lines, boundaries, speeding etc.) is now part of the Kissmyrank Driver's Statistics. Added: Kissmyrank Driving Infraction count is now shown in the Session Results (applies to future sessions). Added: Wins/Podiums/Poles/Fastest Laps/Driving Infractions are now accessible via the "kmr stats" chat command. Added: car list on the Online Web Stats page. Fixed: saving will not work at all when rank.json is empty at start. New "start_money" config.json entry #107 to set the starting amount of money for new players (as it makes more sense to have drivers start at 12000€ and get kicked when they go below 0). Please note that older versions of the plugin were using hardcoded "start_money" = 0 while the new version config.default.json defaults to 12 (thousands). When you add this config line to an existing plugin installation, you should set this to 0 to preserve the old value. If you use the new value, you should tune "min_money" (#26) accordingly.
v1.1 New: Drive-Through penalty support. New: Drive-Through, Kick and Ban from Race Director via Web Browser Race Control. New: "player_give_drive_through" console command. New: track, pit, accessory boundary editing console commands. New: Penalty cost and penalty action maps that allow you to program automatic session based penalties (cost and/or Drive-Through, Kick, Temporary Ban action) for every infraction. New: Pit Area detection (entering and leaving pits). New: Accessory Areas for road junctions etc. for track map completeness. New: Web Track Editor (to be used to view the track and refine the track definitions acquired by driving the car). New: Track Boundary Excluded areas in order to prevent penalties where it makes no sense. New: admins can now send commands to the Kissmyrank console from the Assetto Corsa chat (with password and GUID whitelist). Improved: Race Control Replay car positioning is now more accurate. New: you can now set the length of the Race Control Replays for any given event type. Improved: unified infractions counters. Improved: temporary bans will remain valid if you restart the plugin. Added: "no_money" config.json entry for those who don't like the money system. Improved: time based session timers. Removed: stop and go clear as it was inaccurate and cleared on pitting. Replace your tracks.json with the new one (a huge thanks to Joshuax VGOS for helping with track definitions!). Clear your ~temp.json and your web browser cache for Race Control. Config entries 41, 47, 58-59,80,85-87, 91-92, 97 have been removed. Config entries 108-117 are new. Please update your config.json accordingly.
v1.1a Fixed: Race Director unable to apply a penalty from Race Control when penalty cost is set and penalty action is empty.
v1.1b Fixed: wrong penalty cost displaying for cuts in Race Control. Improved: slightly increased the after-cut replay time for better replays. Fixed: Race Control notifications appearing when the Race Director sets the penalty cost to zero.
v1.1c Improved: removed Magione from the config.default.json rotation list due to standard max_clients exceeding the number of available pit places on this track (if you wish to use this track in the rotation please force max_clients using proper ini_options for all tracks).
v1.1d Improved: no more cuts when going off track in an excluded track boundary area and then rejoining the track at a reasonable speed. New: "max_track_rejoin_speed" config.json entry for the described case. Improved: after-cut replay time is now half of the cut_replay_time (so that it can be controlled from config.json). Config entries 108-109 were updated (for the new track rejoin max speed penalty). Entry 118 is new. Please update your config.json accordingly.
v1.1e New: "race_control_include_players_nearer_than" config entry to determine which drivers should be included in Race Control replays. Improved: nearby players are now detected exactly when the Race Control Event is originated. Fixed: nearby drivers not showing for cuts (this is useful to know if someone was forced off). Improved: no track rejoin penalty if the out of track moment in an excluded area is short (e.g brief excursion out of track on a straight to avoid a crash etc.). Improved: no track rejoin penalty if there are no players nearby (e.g. the track is clear). Fixed: crossing the pit exit line on race start gives a penalty. Fixed: crossing the pit exit line when not in the outlap gives the penalty. Improved: more accurate total driven distance calculation. Improved: stats are now showing infractions per 100km instead of the total number which is not that meaningful to determine a driver's fairness. Improved: cr/100km is now only shown if players have driven at least 1km (to prevent skyrocketing meaningless values). Updated: Imola definitions in tracks.json (excluded the outside area on the straight after the first two turns). New config.json entry 119, please update your config.json accordingly.
v1.1f Fixed: collision count appearing as 0 in the Web Stats Driver View description.
v1.2 Improved: bringing the Track Boundary Cut Penalties to the next level. The detection of a cut is now smarter and processed basing on your driving line as a whole. You will not get a penalty for just crossing an included section of the Track Boundary. You will get it if you do so and rejoin the track without losing time. If you do a mistake like missing the Prima Variante at Monza you now have the chance to avoid the penalty by just slowing down before rejoining the track (e.g. slaloming the signs). The default average speed is the "track_boundary_cut_max_speed" unless the the Track Boundary Cut Gain filter is enabled. New: Track Boundary Cut Gain Filter. The plugin can now analyze your cut and compare it against the fastest lap of the session. In our previous example, this means that if when you cut the Prima Variante you lose enough to fall well behind the ideal section time you will not get a penalty. If you wish to use hardcore detections without filtering, you can just disable this feature by setting "track_boundary_cut_gain_filter" to 0. Added: lap counter to the Race Control Entering and Leaving pits notifications. Added: Cut Type is now shown in the Race Control Cut Replay View. Added: "damage_cost_between_cars_base_speed" and "damage_cost_with_environment_base_speed" config options to allow for a better customization of the damage cost model. Added: "track_boundary_cut_max_time" to set the maximum time frame of a single cut analysis. Updated config.default.json entries 39-40 for the new base speed parameters (since base speed now defaults to 100, I increased these two values to 1). Config entries 120-123 are new. Please update your config.json accordingly.
v1.2a New: "jlp_money_kill_switch" config entry to fully disable the Money/Points system (for leagues, private servers and such). In this configuration you get full Race Control Monitoring and Tracking Features but no money based rewards, fees and penalties. Drive-through, kick and temporary ban penalties are fully available in this mode. New: "rank_sort_by_win_stats" if you wish to sort by win stats rather than money (auto on if you trigger the money kill switch, please also note that if you change this, you should start over with a fresh install of the plugin). Improved: added "track_boundary_cut_gain_filter_min_loss_percent" and "track_boundary_cut_gain_filter_min_average_speed" config entries to give you better control on the cut filter. Added: "pit_speed_limit" config entry to allow you to set the speed inside the pits (this should help to handle the pit speed limiter bug where speed can bounce to 81). Improved: you can now control the qualifying prizes via the new config.json entries (they were hardcoded before). Improved: errors are now written in red. Improved: better troubleshooting info for first time setup connection errros. New: "use money/point system" question added to the First Launch Setup Wizard to make it easier for beginners. New: "driving_line_penalty_repeat_grace" to control the time between to consecutive cutting penalties. config.json entries 124-131 are new. Please update your config.json accordingly.
v1.2b Improved: the plugin will now detect the actual Assetto Corsa Server "MAX_CLIENTS" setting and fix Kissmryank "max_players" as needed. Improved: you can now change MAX_CLIENTS using the track rotation "ini_options" entry (e.g. you can now rotate to tracks with a limited number of slots by forcing the proper MAX_CLIENTS value for the server_cfg.ini, for more please read readme.txt). Improved: added some info regarding path settings to the First Launch Setup Wizard to make it easier for beginners. Config entry 132 is new (no need to set it, if the Assetto Corsa Server results are already properly collected). Please update your config.json accordingly.
v1.2c New: Computer Clock Laptime Validator Anticheat. As an attempt to bring you more reliable leaderboards, Kissmyrank will now compare laptimes posted by the drivers against the clock of the machine where it's running in order to prevent the most blatant CPU clock manipulation abuses. This feature is experimental and only meant for servers that are powerful enough to handle the the API packets with steady delays. Under these conditions it should allow for more reliable leaderboards and fair racing (and if not, it will help to learn more about the reliability of leaderboards). Set config entry 133 to 0 to disable the feature altogether. Config entries 108 and 109 were updated to support the new penalty while 133-134 are new. Please update your config.json accordingly.
v1.3 New: Rolling Start with Formation Lap. Kissmyrank now supports Rolling start with Formation Lap. Positions are locked during the Formation Lap and you can set a higher and lower speed limit. If a driver overtakes and doesn't give the position back within the specified amount of time, he will get a penalty according to the penalty maps (default kick). Rolling start is disabled by default but it can be enabled by setting config entry 135 to 1 (permanent) or using the "rolling_start_toggle" command which applies to future sessions only (and not the current one). New: Virtual Safety Car. This is useful to handle nasty race situations. You can trigger it with the new "virtual_safety_car_deploy" command. During the Virtual Safety Car no overtakes are permitted and all players must respect the specified speed limit. New: you can now choose to use the Virtual Safety Car instead of the Automatic Race Restart when the first lap max collision event is triggered. Fixed: money/points not appearing in the driver Web Stats page when the money/points system is enabled. Config entries 108 and 109 were updated for the new Formation Lap and Virtual Safety Car Penalties. Config entries 135-146 are new. Please update your config.json accordingly.
v1.3a Fixed: "inside ar" error spam. Config entries 108-109 updated for the new Virtual Safety Car and Formation Lap penalties (needed for version 1.3 too). Please update your config.json accordingly.
v1.3b Improved: added more failsafes to prevent people from being kicked for running out of money when "jlp_money_kill_switch" is set to 1.
v1.4 New: support for different languages. Messages sent by the plugin to the online players are now localized using the available language files (please make sure you extract the new "language" folder when you update the plugin). Available translations at this time are English and Italian. Please help translating /languages/en.json to other languages and send me the translated files over Race Department or over the Assetto Corsa forum (please check readme.txt for the translation how-to tips). New: Kissmyrank will now attempt to detect the language when a player connects (language will only be selected if there is a language file for it). New: "kmr language" command that allows players to manually change language. New: "penalty_infraction_map" that lets you choose which infractions increase the infraction counter (which then leads to the "max_infractions" penalty). Improved: you can now set "race_min_players" to 0 if you're not using the money system. Fixed: wrong towing cost calculation. Config entry 147 is new. Please update your config.json accordingly.
v1.4a Fixed: Web Stats pages not working properly in Internet Explorer 11 and below (now they work but without the Race Control Event Viewer, since these old browsers do not support the tools required for it). Improved: slightly increased collision replay time to cover cases in which the moment of the collision would not be captured. Added: German translation kindly provided by Nubb3r. Added: Spanish translation kindly provided by Orcajavi. Please update your language folder with the new files.
v1.4b New: Mass accident detection based on the number of crashing drivers in a specific amount of time (much better than the old blind counter where fights between two players could lead to autorestart). New: you can now have the Virtual Safety Car to be automatically deployed when a mass accident occurs at any lap of the race (for the first lap you can still pick Virtual Safety Car or Auto-Restart using the new config entries). New: "track_boundary_all_track_exclude_left", "track_boundary_all_track_exclude_right", "track_boundary_all_track_include_left", "track_boundary_all_track_include_right" commands to make it easier for long tracks. Added: ks_nordschleife_nordschleife (20+km of boundaries, woot!) to tracks.json (please update your tracks.json accordingly). Added: Czech translation kindly provided by Joshuax VGOS. Improved: the plugin will skip saving tracks.json if it wasn't modified (useful to save some time when you quit). Config entries 48-49 and 136 were removed. Config entries 148-151 are new. Please update your config.json accordingly.
v1.4c Fixed: wrong language autodetection (e.g. fr => es).
v1.5 New: Live Track View. You can now see the cars on the track live with your Web Browser. Just visit the Web Stats Page at http://yourserverip/ and click "Live Map" (the map shows the actual position of every car on the track and not just the progress!). Please keep in mind that the track needs to be included into tracks.json if you want to see it live (capturing a track is easy, just have a look at the readme.txt). Please also note that this is an experimental feature and I haven't tested it with a lot of drivers yet (set config.json entry "live_track_view" to 0 if you wish to disable the feature altogether). Improved: unified cumbersome Race Control Event and Live Track Viewer Zooming Controls into one. Improved: added FPS Limiter to the Race Control Event and Live Track Viewer (in order to save CPU if needed). Improved: you can now change the viewing position and the time scale of a replay without causing an auto-reset every time. Improved: added more troubleshooting information in case of missing language folders/files. Config entry 152 is new. Please update your config.json accordingly.
v1.5a Improved: rendering of Pit and Accessory Areas boundaries now fully includes the captured space (since these areas have walls limiting them and we can't run the capture with the car just outside them, this makes the map more accurate). Fixed: cut lines appearing bigger than they are supposed to be when zooming. Fixed: plugin not quitting properly if no data is present in the leaderboard. Improved: added an option to save the Race Control Event and the Live Map Viewer settings (you can save separate settings for each of the two viewers). Updated: tracks.json with the newest definitions for the default tracks (mostly cosmetic makeup of Pit Entry and Pit Exit Junctions for the new rendering code). Please update your tracks.json accordingly and clear your Web Browser cache.
v1.5b Fixed: Live Map not opening if the first point of the left boundary is not present. Fixed: Live Map not opening if the Kissmyrank Web Admin Console is open.
v1.5c Fixed: Live Map View Driver Auto-Follow dropdown not filling properly on Chrome/Edge. Added: Nordschleife Endurance (25km+ of track boundaries) to tracks.json. Please update your tracks.json accordingly.
v1.5d Added: failsafe for the hot server restart glitch (e.g. cuts being ignored when killing the server and then restarting without any config change). Fixed: Live Map Driver Auto-Follow bugging when reopening after closure.
v1.6 New: Assetto Corsa App Link. This new feature allows Kissmyrank to send events directly to in-game apps without relying on chat messages (e.g. to integrate Kissmyrank events into spotter apps like CrewChief and similar). You can find the documentation under /applink/doc/ and the demo app under /applink/demo/. Fixed: pit detection on some problematic tracks. Fixed: pit exit line crossing before the race starts on some tracks. Improved: Race Control session select dropdown is now sorted to show the most recent sessions first. Improved: added delay for stacked messages at drive time (e.g. each message will be given 1 second to display and newer penalty messages will not be hiding the old ones when coming in groups). Improved: auto race restart now occurs 5 seconds after the notification (in order to allow people with DD wheels to get their hands off the wheel). Fixed: race results showing DNF for lapped cars that finished the race. Added: "Valid Laps" counter to the session results (doesn't include pit inlap and outlap). Fixed: blue flag/hotlap warnings from cars that are in the inlap after completing the session. Added: "track_boundary_set_offset" command to improve rendering of street circuits (e.g. tweak the rendering width for tracks with walls where you cannot run the capture outside the track boundaries). New: Kissmyrank notifications toggle preferences are saved (e.g. if one doesn't want to see Kissmyrank notifications, he don't need to run "kmr toggle_notifications" every time he joins the server). Language files were changed, please update. Config entry 153 is new, please update your config.json accordingly (if UDP port 12002 is in use, please pick a free one and be careful not to reuse the same if you have multiple instances of the plugin running).
v1.6a New: you can now give a drive-through during qualify and practice sessions. Drivers will have to clear that drive-through during the next race. New: "player_cancel_drive_through" command in case you forgot to remove a DT via Race Control in the session in which it was given. New: "player_drive_through_list" command that allows you to list all the drive-through penalties that have not been cleared yet. New: "improving_qualify_laptime_with_infractions" event triggered when someone improves the qualification time with a Kissmyrank cut that is not detected by Assetto Corsa default cut detection. This will help you to make sure that whoever gets a position he doesn't deserve in the Assetto Corsa qualify leaderboard will get a penalty. See config.json entry 155 on how to set a higher laptime cut-off to make this detection less strict. This event is not bound to any penalty by default. You'll need to edit the config.json penalty/infraction maps if you wish to use it (for example mapping it to DT). New: cars.json to convert car ids to human friendly car names (both web and in-game). The file was kindly provided by Orcajavi. Please add it to your Kissmyrank directory. New: Web Admin Console guest login (you need to set both the guest password and the main web admin password in config.json to activate it). Guests will not be able to send any command but they will be able to see the full console output. New: you can now deploy the Virtual Safety Car from Race Control (requires Race Director login, button is near the login button). Added: option not to send the Race Control link when a driver joins. Fixed: saved language and notification preferences resetting on their own. Fixed: "now is undefined" error occurring on certain penalty configurations. Fixed: penalty infraction counter increment not working on some occasions. Improved: better handling of someone entering pits during VSC. Added: "new_session" notification for the AppLink. Fixed: no reply to the "/kmr applink" command when the Kissmyrank Chat Admin feature is enabled. Added: number of laps now appears under the Web Stats Track leaderboard (if you don't reset the stats, the table might look odd till a new track record is posted for that combo, also when using database sharing do not mix 1.6a with past versions, shutdown everything before you update all). Added: French translation kindly provided by EASY. Other language files were modified. Please update all files in your language folder. Added: ks_zandvoort kindly provided by EASY. Improved: prevented previous session delayed collision notifications from appearing on the race grid. New: don't forget to check the new in-game Kissmyrank Spotter App that comes with the package (it's inside the app folder). Thanks to Joshuax VGOS for kindly providing the images for the app. Feel free to provide alternative image packs so that I can include them. Config entries 108-109 and 147 were updated for the new infraction event. Entries 154-156 are new. Please update your config.json accordingly.
v1.6b New: penalty event when a car is parked in proximity of the track for a prolonged period (to prevent trolls from blocking the track). It's mapped to some penalties in the default config. Please change the mapping according to your needs (or disable it via the provided config options). Improved: ping deviation kick will not occur if the ping is consistently going down over the last 4 measurements (useful when ping is stabilizing after joining). New: "tracks_list", "tracks_import", "tracks_export" commands. To import some tracks place the json file containing them in the "import" folder and run the "tracks_import file.json" command. To export some tracks run the "tracks_export monza_|mugello|ks_silverstone_national" command with the ids of the tracks that you would like to export. You'll then find the resulting file in the "export" folder. Make sure you create the "import" and "export" folders when you update existing installations of the plugin. Fixed: an "undefined" error that could pop up if one of the penalty/infraction maps was not defined (this won't make the penalties working if the entries are missing but just remove the error spam when a driver gets the penalty). Fixed: web stats not loading in some browsers. Updated: language files. Please overwrite the whole folder. Fixed: only the first mapped penalty is processed for a certain event (e.g. cannot kick and charge a cost at the same time). Updated: config entries 108,109 and 147 for the new penalty. Improved: added a fallback for the detection of the public IP at start for a better App Link experience. New: config entries 157-159. Please update your config.json accordingly.
v1.6c New: "player_parking_permit_toggle" console command (for a better track recording experience when parking_near_track penalties are enabled). Improved: new players leaving the server without spawning to the track will not be added to the stats table (good to save database space and also for people that might want to leave the server without being logged). New: "driver_privacy_erase_personal_data_and_ban" console command that you can run if any person ask you to comply with his right to be forgotten. New: "driver_privacy_cancel_ban" console command which can be used to unban a player that previously decided to clear its data (players that make use of their right to be forgotten are banned using a hash since otherwise they could just clear their data and abuse in loop). New: players might use the "kmr erase_my_personal_data_and_ban_myself" chat command to remove their personal info (this command disabled by default, you can enable this command using config #160 if you need it). Updated: language files. Please overwrite. When using database sharing, do not mix with previous versions of the plugin. Config entry 160 is new. Please update your config.json accordingly.
v1.6d Improved: disabled idle auto-save tracks.json when database sharing is enabled (since track updates propagate to every client, tracks.json would be frequently saved on all servers).
v1.6e New: "drive_through_no_kick" config option to disable the kick penalty when a DT is not cleared or when two DT events occur in a row.
v1.6f Fixed: "player_cancel_drive_through" console command not working.
---------------------------------------------
Have fun!
Brioche