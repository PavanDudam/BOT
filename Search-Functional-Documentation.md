# Athlyte Search Application - Functional Specification

Website link: search.athlytesports.com

## 1. Introduction

### 1.1 Objective

This document outlines the functional specifications for Athlyte’s Search Feature. Its primary purpose is to provide a clear understanding of what the application is designed to do, its capabilities, and its current limitations.

## 2. Scope

The Athlyte Search Feature is designed to enable a natural language search interface for sports data and statistics. It supports queries related to entities like player and team performance across sports like
- Men’s Football (MFB)
- Men’s Basketball (MBB)
- Women’s Basketball (WBB)
- Men’s Ice Hockey (MIH)
- Women’s Ice Hockey (WIH)
- Men’s Soccer (MSO)
- Women’s Soccer (WSO)
- Men’s Volleyball (MVB)
- Women’s Volleyball (WVB)
It includes:
- Integration with primary data sources (Genius and Recordbook).
- Supported sports, entities, query types, and data periods.
- Data processing, normalization, and known reliability aspects.
- Key application modules and background data processing flows.

## 3. Detailed Functional Requirements

### 3.1 Data Management

#### 3.1.1 Data Sources

The Athlyte Search Application currently utilizes data from three primary sources:

- Genius: Provides all sports stats for NCAA colleges from 2014 to present.
- Recordbook: Contains historical and record-breaking data (published by colleges).
- Stat Crew: Has sports statistical data from 1997-2014

#### 3.1.2 Data Scope by Source

Genius Data:
- Timeframe: Data availability changes as per sport.

| Sport | Standard Data Range |
| --- | --- |
| Men's Football | 2014 – Present |
| Men’s Basketball / Women’s Basketball | 2009 – Present |
| Men’s Ice Hockey / Women’s Ice Hockey | 2015 – Present |
| Men’s Soccer | 2013 - Present |
| Women’s Soccer | 2015 - Present |
| Men’s Volleyball | 2016 - Present |
| Women’s Volleyball | 2015 - Present |

- Colleges: Data from all colleges available in Genius has been taken.
Recordbook Data
- Data Availability Timeframe: varies with college
- Data Required: prior to 2014
- Colleges: Only the colleges that have record books.
- Stat Coverage: Only includes records (e.g. top 10 highest rushing yards) and not all the stats of the games.
- In the new record book process, a hybrid approach is being followed where data extraction is done using Label Studio (a tool used for annotating data), and the verification of the extracted data is done manually.
- Currently, 250 record books have been processed. This method allows us to process 500 record books with a 5% false positive rate, significantly increasing our data extraction capabilities.
- We are not capturing all the data from the record books, there’s a master record list that we follow for this;
Data:
This document provides a comprehensive list of all the stats exposed to Search
Data Sources

#### 3.1.3 Data Normalization & Modifications

The application performs certain data modifications and normalizations:
- Data Normalization: All the player data is retrieved from Genius, but not as it is. We normalize it first into a desired format, only for player class and player position. We also compute some additional stats that aren't available on Genius, using the raw data we get from them.
- Computed Stats: Certain statistics are computed by the system, here we have the underlying data:

- Period Data Aggregation: Period-level data (quarter-level for Men’s Football; half-level for Men’s & quarter-level for Women’s Basketball) is summed up and compared against game-level data.

#### 3.1.4 Athlyte Query Language (AQL)

Here a natural language query is transformed into a structured query language (Athlyte Query Language) that a computer program or database can easily understand and execute to fetch the correct information.
This is the standard format for AQL:
{"query_type": , "entity": , "qualifiers": , "stat_period": , "conditions": , "streak_len": , "periods":, "period_type": }
Example:
User Query: The highest punt returns yards accomplished during a season
AQL : {"query_type": "max", "entity": "player", "qualifiers": {}, "stat_period": "season", "conditions": "s_punt_returns_yards", "streak_len": null, "periods": null, "period_type": null}

| query_types | entity | qualifiers | stat_period |
| --- | --- | --- | --- |
| basic | player | player position | quarter |
| min | team | player class | half |
| max |  | team conference name | game |
| ltw |  | opponent conference name | season |
| streaks |  | opponent team name | career |
|  |  | home/away |  |
|  |  | win/loss |  |
|  |  | team name |  |
|  |  | player name |  |
|  |  | division |  |

The following parameters are followed for the current AQL format:
“conditions”: “”,
“entity”: “player | team”,
“period_type”: “regular | overtime”,
“periods”: “”,
“stat”: “<stat_id> (e.g. s_rushing_yards, s_kick_returns_average)”,
“qualifiers”: {
“team”: {
“team_name”: “”,”
“conference”: “”,
“division”: “”
},
“opponent”:{
“opp_team_name”: “”,
“opp_conference”: “”,
},
“division” : “”,
“player_filters”: {
“player_name”: “”,
“player_class”: “freshman | sophomore | junior | senior”,
“position”: “RB | QB | OC | ...“,
},
“game_filters”: {
“result”: “win | loss”,
“game_type”: “regular | post_season”,
},
},
“query_type”: “max | min | basic | ltw | streak”,
“stat_period”: “quarter | half | game | season | career”,
“streak_length”: “”
New AQL:
The following parameters are followed for new AQL format in Search R3.5 :

| query_types | entity | qualifiers | stat_period |
| --- | --- | --- | --- |
| basic | player | player position | quarter |
| min | team | player class | half |
| max | coach* | team conference name | game |
| ltw |  | opponent conference name | season |
| streaks |  | opponent team name | career |
| count* |  | home/away |  |
| rank* |  | win/loss |  |
| trend* |  | team name |  |
|  |  | player name |  |
|  |  | division |  |
|  |  | starter* |  |
|  |  | venue* |  |
|  |  | home/away* |  |
|  |  | win/loss* |  |
|  |  | game_type* |  |
|  |  | game* |  |

{
"query_type": "max | min | basic | ltw | streak | count | rank | trend | average | sum",
"entity": "player | team | coach",
“period_type”: “regular | overtime”,
"stat": "<stat_id> (e.g. s_punts_yards, s_kick_returns_average)",
"qualifiers": {
"team": {
"team_name": "","
"conference": "",
"division": ""
},
"opponent":{
"opp_team_name": "",
"opp_conference": "",
},
"player_filters": {
"player_name": "",
"opponent_player_name": "",
"class": "freshman | sophomore | junior | senior",
"position": "rb | qb | oc | ...",
"starter": true
},
"game_filters": {
"venue": ""
"at": "home | away | neutral",
"result": "win | loss",
"game_type": "conference | bowl | playoff | championship | exhibition"
"game": "regular | post_season",
},
},
"season" : {
"n": "-3",
"start": "",
"end": "",
},
"game": {
"n": "-4",
"start": "",
"end": "",
},
"period": {
"index":["1", "2"]
},
“stat_period”: “quarter | half | game | season | career”,
"conditions": "",
"streak": {
"length": 5,
"domain" : 10*,
"direction": "consecutive | non_consecutive",
"unit": "season | game"
},
"sort": {
"by": "stat | streak_length | date",
"direction": "asc | desc"
},
"rank": {
"position": 2,
"order": "asc | desc"
},
"limit": 10
}

### 3.2 Search Application Features

#### 3.2.1 Dashboard

- Sports & Entities:
The search application allows users to search within the following sports and entities:

#### 3.2.2 Query Types

The application supports the following natural language query types:

- All queries support only 1 period at a time.

| Query Type | Number of Stats | Qualifiers | Periods | Examples |
| --- | --- | --- | --- | --- |
| Stat Search (Basic) | Single Stat | ✓ | ✓ | Players with rushing yards greater than 10. |
| Stat Search (Complex) | 1 to 3 Stats | ✓ | ✓ | Teams with at least 20 passing attempts and three field goals made in a game. |
| Records (Maximum) | Single Stat | ✓ | ✓ | Highest number of touchdowns scored. |
| Records / (Minimum) | Single Stat | ✓ | ✓ | Line Backers with lowest number of touchdowns in a season. |
| Last Time | Up to 3 Stats | ✓ | ✓ | Last time any team had at least 3 touchdowns in a game. |
| Streaks | 1 or 2 Stats | ✘ | Game only | Players with 12 receiving yards over 6 consecutive games. |
| Count |  |  |  | In how many games did Bryce Young have greater than 80 rushing yards |
| Rank |  |  |  | Players at the 9th-most rushing yards in 1st quarter |
| Trend |  |  |  | Is Alabama's rushing yards on the rise in a season during the regular season |
| Average |  |  |  |  |
| Sum |  |  |  |  |

#### 3.2.3 Qualifiers

Qualifiers allow users to narrow down search results based on specific criteria. The following qualifiers are supported:

- Applicability: Qualifiers are applicable to all query types except Streak queries.
- Multiple Qualifiers: Users can apply more than one qualifier in a single query.

#### 3.2.4 Scope

Queries support data retrieval for only one specified time period at a time, meaning you cannot request data for multiple periods within a single query.

#### 3.2.5 Supported Stat Periods

The granularity of data for search results varies by query type and sport:

| Query Type | Supported Period / (MFB) | Supported Period (MBB) | Supported Period (WBB) |
| --- | --- | --- | --- |
| Basic | Quarter, Half Game, Season, Career | Half, Game, Season, Career | Quarter, Half, Game, Season, Career |
| Records | Quarter, Half, Game, Season, Career | Half, Game, Season, Career | Quarter, Half, Game, Season, Career |
| Last Time Whens (LTWs) | Quarter, Half, Game, Season, Career | Half, Game, Season, Career | Quarter, Half, Game, Season, Career |
| Streak | Game | Game | Game |

#### 3.2.6 Result Screen

After performing a search query, you will be directed to a results screen. This page displays a list of players, detailing their class, position, opposing teams, game outcomes, and the conference affiliation. Additionally, the page offers various filters to further refine the search results.

| Result Screen Contents | Quarter/Half | Game | Season | Career |
| --- | --- | --- | --- | --- |
| Player name | ✔ | ✔ | ✔ | ✔ |
| Player class | ✔ | ✔ | ✔ | ✘ |
| Player position | ✔ | ✔ | ✔ | ✔ |
| Game Date | ✔ | ✔ | ✘ | ✘ |
| Season | ✘ | ✘ | ✔ | ✘ |
| Team | ✔ | ✔ | ✘ | ✔ |
| Opponent | ✔ | ✔ | ✘ | ✘ |
| Result | ✔ | ✔ | ✘ | ✘ |
| Opponent Conf. | ✔ | ✔ | ✔ | ✔ |
| Period type | ✔ | ✘ | ✘ | ✘ |
| Period number | ✔ | ✘ | ✘ | ✘ |
| Stat value | ✔ | ✔ | ✔ | ✔ |

#### 3.2.7 Filters

The search application includes a range of filters to further refine search results.

| Filter | Function |
| --- | --- |
| Opponent Conference | Filter results based on the selected opponent's conference. |
| Opponent | Select a specific opponent team to filter the matches |
| Results | Filter by match result |
| Game Type | Filter based on the type of game (Regular, Postseason) |
| Period Type | Filter results by the time period |
| Date | Specify a custom date range to narrow down the results by match date |
| Name | Search for a specific player by name |
| Position | Filter players based on their playing position |
| Classes | Filter players by class year |

The filters are applicable to all the query types except Streaks.

| Filter Contents | Quarter/Half | Game | Season | Career |
| --- | --- | --- | --- | --- |
| Opponent Conf. | ✔ | ✔ | ✘ | ✘ |
| Opponent | ✔ | ✔ | ✘ | ✘ |
| Results | ✔ | ✔ | ✘ | ✘ |
| Game Type | ✔ | ✔ | ✘ | ✘ |
| Period Type | ✔ | ✔ | ✔ | ✔ |
| Name | ✔ | ✔ | ✔ | ✔ |
| Position | ✔ | ✔ | ✔ | ✔ |
| Classes | ✔ | ✔ | ✔ | ✔ |
| Date Range | ✔ | ✔ | ✘ | ✘ |

#### 3.2.8 Queries

### 3.3 Application Features

#### 3.3.1 Player Dashboard

The player dashboard consists of the following functionalities:

Player Statistics
The "Player Statistics" section of a player's dashboard offers an overview of the seasonal stats of the player . The aggregate statistics for every season can be viewed.
Filters: These stats can be filtered based on season, stat, and stat category.
Player Records
This page details a player's individual performance, including their stats, value, rank, and the stat value of the rank above. It also displays the game date for each statistic and the opponent's team.
Filters: These stats can be filtered based on period, season, stat, and stat category.
Season & Career Highs
This displays the highest score achieved by a player for each statistic, either in a single season or across their entire career, as well as the game date on which it was scored.
Filters: These stats can be filtered based on period (season/career), stat, and stat category.
Player Game Log
Gives a complete list of all games played by a player in a season, including the opposing team for each game.
Filters: These stats can be filtered based on season, stat, and stat category.
Player Streaks
Player Streaks provides information on a player's statistical performance for all stats across consecutive games.

#### 3.3.2 Game Dashboard

Player Stats
Provides a detailed breakdown of individual player statistics for both teams in the game.

Filters: A "Category:" dropdown allows users to change the type of statistics displayed (e.g., passing, rushing, receiving, etc.).

Team Stats
It provides a side-by-side comparison of various statistical categories for both team and opponent team for the specified game.

Rosters
The "Rosters" tab of the game dashboard, provides a list of players for both competing teams during this specific game.

Play-by-Play
This gives a detailed description of every action, movement, and event of a match.

Filters: A "Show" dropdown allows users to filter the roster between starters and the full roster.

Revisions in R2
- In the new process, data extraction from the record books is mostly automated, with manual intervention required only for verification.
- This process, called the match process, involves manually comparing the extracted data with the data in the record to check for inconsistencies.

### 3.4 R3 Features

#### 3.4.1 Team Dashboard

Team Statistics
The "Team Statistics" section of a team's dashboard offers an overview of the seasonal stats of the team. The aggregate statistics for every season can be viewed.

Filters: These stats can be filtered based on season, stat category, and substat.

Team Records
This page details a team's performance, including the stat name, value, rank, and the stat value of the rank above. It also displays the game date for each statistic and the opponent's team.

Filters: These stats can be filtered based on period, season, stat category, and substat.

Season Highs
Displays the highest value achieved by the team for each statistic in a season, as well as the game date on which it was recorded.

Filters: These stats can be filtered based on season, stat category, and substat.

Team Game Logs
Gives a complete list of all games played by the team in a season, including the opposing team, result, and score for each game.

Filters: These stats can be filtered based on season, stat category, and substat.

Team Streaks
Team Streaks provides information on a team's statistical performance for all stats across consecutive games.

#### 3.4.2 Visualize Data

The "Visualize Data" feature adds simple visual representations to search results. After performing a search, users can click the "Visualize Data" button near the results table to display a chart based on the selected query and relevant period (game or season).

Simple: For basic queries (e.g., "players with rushing yards > 50"), a horizontal bar chart shows the top 10 players who met the condition the most number of times. No. of occurrences shows how often each player achieved the stat.
Complex: For queries with more than one condition (e.g., "players with rushing yards > 50 and passing yards > 10"), a scatter plot shows the top 10 players who met both conditions most frequently.

Records (Min & Max): For record-based queries (e.g., "highest rushing yards in a game"), a line chart takes the first 10 entries from the results table (even if the same player appears more than once) and plots each player's record game in the center, with up to 3 games before and 3 games after.

Last Time When: In last time when queries, a line chart picks the unique players from the results and plots up to 10 of their games.
Streaks: For queries tracking consecutive-game performance (e.g., "players with > 50 rushing yards in consecutive games"), a line chart plots the stat value across each game in the streak, with the streak length indicated next to each player's name.

#### 3.4.3 Typeahead

Typeahead adds real-time autocomplete to the existing search experience. As a user types into the search box, a dropdown appears beneath it showing matching suggestions they can pick from instead of typing the full query.

#### 3.4.4 Ask Athlyte

The Ask Athlyte Bot is a personal sports analytics assistant integrated into the platform. It helps users explore stats, frame sports queries effectively to get the best results from the Athlyte search feature, and answer any questions about how to use the platform.

### 3.5 User Onboarding & User Management via Admin Panel

The Admin Panel provides functionalities for system administration:
- User Onboarding via User Dashboard
- User onboarding via the user dashboard, the following flowchart explains how a user can sign from his end.

- Case 1: If the user’s college is enabled  with Athlyte, they can directly register with us by sending a sign-up request.

Once the request is approved by the admin, users will be able to sign in.
- Case 2: If a user's college isn't enabled, they can send an email to request its enablement.

The admin will then add the college and notify the user that they can now send a sign-up request to register with us.

Once the admin approves the request, the user will receive an email suggesting they will be able to sign in.

- User Onboarding via Admin Dashboard
The admin dashboard is used to add new users, update existing user profiles, accept/reject pending approval requests, and view a complete list of all users.

- Team Onboarding : This refers to integrating a college team into the platform's dashboard. It is done by the admin via the admin portal.
- This process essentially includes adding their recordbooks and ongoing sports performance data (Genius) for further processing.
- A user can sign up only if the team onboarding has been completed.

- User Management:

| Feature | Function |
| --- | --- |
| Create User | Add new users |
| Update User | Update existing user profiles |
| Pending Approvals | Accept/reject pending approval requests |
| All Users | View a complete list of all users. |
| Team Onboarding | Adding a college team into the platform's dashboard. |

### 3.6 Background Data Processing

#### 3.6.1 Postgame Processor

- Function: Automatically updates game, season, and career statistics for both players and teams after games occur.
- Process: Runs in the background, checking for updated games every hour (within a weekend timeframe).

#### 3.6.2 Preseason Processor

- Function: Prepares data before the start of a season.
- Process: Scrapes all schedules and rosters from Genius to update relevant database tables.
