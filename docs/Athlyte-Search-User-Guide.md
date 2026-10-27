# Athlyte Search User Guide

## Athlyte Search Overview

Athlyte Search is a natural language interface that allows you to find sports data by simply typing questions or statements. Instead of navigating complex databases, you can search for player and team performances across Men’s Football (MFB), Men’s Basketball (MBB), and Women’s Basketball (WBB).

## Supported Sports

The application currently supports deep statistical searching for:
- Men’s Football
- Men’s Basketball
- Women’s Basketball
- Men’s Ice Hockey
- Women’s Ice Hockey
- Men’s Soccer
- Women’s Soccer
- Men’s Volleyball
- Women’s Volleyball

Note: We are working hard to bring you even more data! Support for additional sports will be added in future updates.

## Data Origins and Availability

Our statistics come from three primary sources, each covering different timeframes:

| Sport | Coverage |
| --- | --- |
| Men's Football | 2014 to Present |
| Men's Basketball | 2009 to Present |
| Women's Basketball | 2009 to Present |
| Men's Ice Hockey | 2015 to Present |
| Women's Ice Hockey | 2015 to Present |
| Men's Soccer | 2013 to Present |
| Women's Soccer | 2015 to Present |
| Men's Volleyball | 2016 to Present |
| Women's Volleyball | 2015 to Present |

- Pre-2014: Powered by official College Recordbooks. This data focuses on historical records (like "Top 10 All-Time") and varies by school. We manually verify this data to ensure accuracy.

## Query Categories

You can perform five different types of searches:

- Basic Search: Simple lookups for single statistics.
- Example: "Players with rushing yards greater than 10."
- Complex Search: Combining 1 to 3 different stats in one search.
- Example: "Teams with 20+ passing attempts and 3+ field goals made in a game."
- Record Search (Maximums & Minimums): Finding the highest or lowest values ever recorded.
- Example: "Highest number of touchdowns scored" or "Lowest turnovers by a guard in a season."
- Last Time When (LTW): Looking up the history of a specific event.
- Example: "Last time any team had at least 3 touchdowns in a game."
- Streak Search: Tracking consecutive performances over multiple games.
- Example: "Players with 12+ receiving yards over 6 consecutive games."

## Search Power Tools: Qualifiers

You can narrow down your results using specific filters directly in your search text:

- Team & Opponent: Filter by team name, conference (e.g., SEC, ACC), or division.
- Player Attributes: Filter by player name, class (Freshman, Sophomore, Junior, Senior), or position (QB, RB, Guard, etc.).
- Game Context: Search by game result (Win/Loss) or game type (Regular season vs. Post-season).

## Navigating Your Results

After you search, the Results Screen displays a list of matches with key metadata such as player class, position, opposing teams, and game outcomes.

### Sidebar Filters

You can refine your results instantly using the sidebar without re-typing your query. These filters apply to all query types except Streaks:

- Opponent & Conference: Filter by a specific opponent team or an entire conference (e.g., SEC, Big Ten).
- Game Result: Narrow results to only Wins or Losses.
- Game Type: Toggle between Regular Season and Post-season games.
- Date Range: Specify custom start and end dates to see stats from a particular timeframe.
- Player Metadata: Filter by Name, Position (e.g., QB, Guard), or Class year (Freshman, Sophomore, Junior, Senior).
- Period Type: Filter by specific parts of the game like first half or overtime.

### Player Dashboard

Clicking on any player's name opens their dedicated dashboard, which is broken down into several powerful sections:

- Player Statistics: A seasonal overview showing aggregate stats for every year of their career. You can filter these by season and category (e.g., Passing, Defense).
- Player Records: A deep dive into individual game performances. This section shows the player's rank for specific stats and even identifies the "value to beat" for the rank immediately above them.
- Season & Career Highs: Quickly view the best mark a player has ever achieved in a single game, either within a specific season or across their entire career, including the date and opponent.
- Player Game Log: A complete list of every game played in a selected season, providing a chronological view of their performance.
- Player Streaks: Analyzes performances across consecutive games to identify consistent high-level play.

### Game Dashboard

Accessible from the search results, this dashboard provides a complete breakdown of a specific matchup:

- Individual Player Breakdown: Detailed statistical performance for every player on both teams for that specific game. Users can switch between stat categories (e.g., Rushing vs. Receiving) using a dropdown.
- Team Stats Comparison: A side-by-side view of team-level statistics, allowing you to compare how the home and away teams performed across all categories.
- Game Rosters: View the full list of players available for both teams. A toggle allows you to switch between viewing only the starters or the full roster.

## Account Access and Team Onboarding

Access to the application is managed through a simple process:

- Self-Registration: If your college is already enabled, you can sign up directly. Once an admin approves your request, you can log in.
- Requesting a Team: If your college isn't listed, contact us to begin the "onboarding" process. We will integrate your official recordbooks and live Genius data into the platform.

## Automated Data Updates

To keep everything current, our background processors run constantly:

- Postgame Processor: Updates all game, season, and career stats automatically every hour during active game weekends.
- Preseason Processor: Scrapes new schedules and rosters before the season starts so every new player is searchable immediately.
