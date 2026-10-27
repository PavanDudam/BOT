# Athlyte Search — Navigation Guide

This document describes how an end user navigates the Athlyte Search application page-by-page. Each section lists the page's elements that live on it, and the click-by-click steps required to use every feature exposed there.

## Table of Contents

- Onboarding Wizard
- Dashboard
- Full Schedule Page
- Game Dashboard
- Search Result Screen — Player
- Search Result Screen — Team
- Player Dashboard
- Team Dashboard
- Search Information Centre (Help)
- Plans & Upgrade Flow
- Checkout Flow
- Common UI Elements

## 1. Onboarding Wizard

Trigger: First login or any login that has not yet completed the onboarding tour.

The wizard appears as a modal/tooltip overlay with a primary "Next" button.

### Step-by-step navigation

- After login, the wizard auto-opens on the Dashboard.
- Click Next (Step 1 of 2) to advance.
- Click Next (Step 2 of 2) if applicable.
- Click Finish on the final step.

To dismiss the wizard programmatically, the suite repeatedly clicks the primary CTA up to four times.

## 2. Dashboard

The Dashboard is the central hub. It hosts global navigation, the search bar, "Recent Searches", and "Upcoming Games".

### Header (top bar)

| Element | Location | Purpose |
| --- | --- | --- |
| Athlyte logo | Top-left (link Athlyte logo) | Returns to Dashboard from any page |
| Sport switcher | Center-left | Switches stat domain: Football, Basketball (M), Basketball (W), Ice Hockey (M), Ice Hockey (W), Soccer (M), Soccer (W), Volleyball (M), Volleyball (W) |
| Help icon (?) | Right side | Opens the Search Information Centre |
| Profile button | Top-right | Opens the user profile dropdown |

### Profile dropdown — step-by-step

- Click the profile element at the top-right (the username + dropdown arrow).
- The dropdown appears containing three items:
- Dashboard — clicking returns to Dashboard
- Profile — opens the profile dashboard showing account details, current subscription plan, active sports, and options to upgrade (add new sports or add-ons).
- Sign out — clicking logs the user out and redirects to Login
- To sign out: click profile → click Sign out → wait for the URL to change to Login.

### Upgrade button — step-by-step

An Upgrade button is visible in the top-right corner of the screen.

- Click Upgrade. The plan-selection page will open.
- Confirm that every visible button on the page is an active CTA — every button should be clickable and respond when tapped. If a button appears greyed-out or unresponsive, refresh the page before continuing.

### Change Plan — step-by-step

- From the Dashboard, click Change Plan.
- The plan-selection page used during the original upgrade flow opens.
- Select a different sport or adjust add-ons, then complete the payment steps (see Plans & Upgrade Flow).

### Sport switcher — step-by-step

- Locate the sport buttons in the header navigation (Football, Basketball, Ice Hockey, Soccer, Volleyball).
- Click Football to switch to MFB stats.
- Click Basketball to expand into MBB sub-options. If sub-buttons appear, click Basketball (M) or Basketball (W) to choose the variant.
- Click Ice Hockey to expand into MBB sub-options. If sub-buttons appear, click Ice Hockey (M) or Ice Hockey (W) to choose the variant.
- Click Soccer to expand into MBB sub-options. If sub-buttons appear, click Soccer(M) or Soccer(W) to choose the variant.
- Click Volleyball to expand into MBB sub-options. If sub-buttons appear, click Volleyball (M) or Volleyball(W) to choose the variant.
- After switching, the search bar placeholder updates and Trending/Recent Searches re-populate for the selected sport.

### Search bar — step-by-step

The search bar lives in the main body. Its placeholder is Start by typing [e.g. Players with field goals made > 25].

- Above the search input there are two toggles: Player and Team. Click Player to query player stats; click Team to query team stats.
- When Player is active, the placeholder reads Players with field goals made > 25.
- When Team is active, the placeholder reads Teams with field goals made > 25.
- Click into the search bar and type a natural-language query, e.g. Players with points per game > 20.
- Press Enter or click Search to submit.
- On success, the app navigates to the Search Result Screen and shows Results found (or a transient Searching... state).
- If the field is empty when Enter is pressed, the system shows a warning ("please search something").

### Recent Searches — step-by-step

- Scroll to the Recent Searches section on the dashboard.
- Each card is a clickable div containing a sample query (e.g. Players with > 50 Longest Field Goal Made in a game).
- Click any card to auto-populate the search bar with that query.
- To return to the dashboard, click the Athlyte logo in the header.

### Upcoming Games widget — step-by-step

- Scroll to the Upcoming Games section.
- If games exist, you see one or more cards reading vs <Opponent> | <Stadium> | <Date>.
- Click any card to navigate to that game's Game Dashboard (the page shows the same opponent name from the card).
- If no upcoming games exist, the empty state displays No upcoming matches found (or No upcoming games).
- Click View Full Schedule` for the full season list.

### Help icon — step-by-step

- Click the ? help icon in the header.
- The browser navigates to the Search Information Centre (a separate page).

## 3. Full Schedule Page

Reached by clicking View Full Schedule under the Upcoming Games widget on the Dashboard.

### Step-by-step navigation

- From the Dashboard, click View Full Schedule.
- Click any individual game card to open the Game Dashboard.

## 4. Game Dashboard

The Game Dashboard shows the head-to-head detail for a single game.

### Layout

- Team logos — home team logo on the left, opponent logo on the right.
- Team names — printed below each logo.
- Total score — large number(s) between the two logos.
- Game Info bar — four labeled cells:
- VENUE
- ATTENDANCE
- DATE
- SEASON
- Action buttons — PLAYER STATS, TEAM STATS, ROSTER, PLAY-BY-PLAY.

### Step-by-step navigation

#### Via Result Screen

- Search for a query (e.g., "players with more than 2 touchdowns in a game")
- From the results table, click the hyperlinked date in the DATE column to open that game
- Click PLAYER STATS to view the per-player breakdown for this game.
- Click TEAM STATS to view the team-level box score.
- Click ROSTER to view the lineup of players who participated.
- Click PLAY-BY-PLAY to view detailed description of every play of the match

#### Via Dashboard

- From the Dashboard, click View Full Schedule.
- Click any individual game card to open the Game Dashboard.
- Click PLAYER STATS to view the per-player breakdown for this game.
- Click TEAM STATS to view the team-level box score.
- Click ROSTER to view the lineup of players who participated.
- Click PLAY-BY-PLAY to view detailed description of every play of the match

## 5. Search Result Screen — Player

The Result Screen shows tabular data for the query, with filters, export, and reporting controls.

### Top of page

- Total results count (e.g. 42 Results found).
- Export button (top of the table) — downloads the current table to Excel.
- Report button (top right of the dashboard area) — opens the bug report modal.

### Filters panel (left side)

The filters available depend on the query type. A persistent Apply Filters button sits below the panel.

| Query type | Filters shown |
| --- | --- |
| Quarter / Half / Game | Opponent Conference, Opponents, Results, Game Type, Period Type, Name, Position, Classes, Date |
| Season | Period Type, Name, Position, Classes |
| Career | Period Type, Name, Position, Classes |

Each filter is a multi-select dropdown. To use:

- Click the dropdown trigger (e.g. Select Opponent Conference) to expand the option list.
- Tick the checkbox next to each value you want.
- Click anywhere outside to close the dropdown.
- Click Apply Filters below the panel — the table reloads with the filtered rows.
- To clear a filter, reopen the dropdown and untick the value (or click the x badge next to the selection), then click Apply Filters again.

### Results table

Column headings (Quarter / Half / Game queries): ID, Player, Class, Pos, Date, Team, Opponent, Result, Period Type, Data Source, Opponent Conference,Period Number (for half/quarter), {Stat}

Column headings (Season query): ID, Player, Class, Pos, Season, Team, Period Type, Data Source, {Stat}

Column headings (Career query): ID, Player, Class, Pos, Team, Period Type, Data Source, {Stat}

#### Step-by-step actions on the table

- Sort — click any column heading to toggle ascending/descending sort on that column.
- Search by name — click the Name bar and look
- Pagination — scroll to the bottom of the table and use the page size selector (e.g. 10/25/50/100) to change rows per page; the table updates accordingly.
- Open a player dashboard— click a player's name in the table to navigate to their Player Dashboard.
- Open a team dashboard— click a team's name in the table to navigate to their Team Dashboard.
- Open a game dashboard— click a game date in the table to navigate to their Game Dashboard.
- Export — click Export at the top of the table; the browser downloads an Excel file containing the same rows currently displayed (subject to filters).
- Visualize Data — click Visualize data  near the table to open a chart panel.

### Step-by-step (typical workflow)

- Run a search from the Dashboard (e.g. Players with points per game > 20).
- The Result Screen opens with a table of matching rows.
- Read the Total results count at the top.
- Apply filters from the left panel (e.g. select an Opponent Conference) and click Apply Filters.
- Click a column header to sort.
- Click a player's name to open their profile, or click Export to download the current view.

## 6. Search Result Screen — Team

The Team result screen has the same structure as the Player result screen — header, filters, table, export, report — but the rows are aggregated to team level.

### Differences from Player view

- The toggle on the Dashboard must be set to Team before submitting the query.
- Some filters that apply only to players (Position) will be hidden.
- The "Career" period is not offered for Team queries — Team queries support Game, Half, Quarter, and Season periods only.

## 7. Player Dashboard

### Step-by-step navigation

- Search for a query (e.g., "players with more than 2 touchdowns in a game")
- From the results table, click the hyperlinked player name in the PLAYER column to open that player dashboard.
- Click PLAYER STATISTICS to view the player's aggregate stats by season.
- Click PLAYER RECORDS to view the player's game, season, and career records with rankings.
- Click SEASON AND CAREER HIGHS to view the highest value the player has recorded for each stat.
- Click PLAYER GAME LOG to view a game-by-game breakdown of the player's performance.
- Click PLAYER STREAKS to query consecutive-game streaks for any stat threshold.

### Tab navigation (top of body)

Five primary action buttons:

- PLAYER STATISTICS
- PLAYER RECORDS
- SEASON AND CAREER HIGHS
- PLAYER GAME LOG
- PLAYER STREAKS

Click any button to switch tabs; the body updates to the corresponding panel.

### 7.1 Player Statistics tab

- Click PLAYER STATISTICS in the header.
- The body shows a table with SEASON and one column per stat.
- Filter the data using three dropdowns at the top of the table:
- Select Season — pick one or more seasons to limit the rows.
- Select Category — pick a stat category (e.g. Passing, Rushing).
- Select Substat — pick specific stats within the category. Multi-select supported.
- Click any column header to sort the table.
- The TOTAL row at the bottom of the table reflects the cumulative values for the visible rows.
- All decimal values are rounded to two decimal places.
- To clear a selection: click the x next to the selected value (clearing a category also clears its substats; clearing the season resets the table to defaults).

### 7.2 Player Records tab

- Click PLAYER RECORDS in the header.
- A scope dropdown labelled game appears on the right side above the table. Click it to choose:
- game — game-level records (default)
- season — season-level records
- career — career-level records

#### Player Records — Game

Table columns: Season, Stat Name, Value, Rank, Next Rank Value, Game Date, Opponent Team. Filters: Select Season, Select Category, Select Substat (same multi-select pattern as 8.1).

#### Player Records — Season

Table columns: Season, Stat Name, Value, Rank, Next Rank Value. Filters: Select Season, Select Category, Select Substat.

#### Player Records — Career

Table columns: Stat Name, Value, Rank, Next Rank Value. Filters: Select Category, Select Substat (no season filter — career is cumulative).

For all three sub-tabs:

- Click a column header to sort.
- Click a dropdown to expand options; tick a value to filter; click x to remove the filter.
- Decimal values are rounded to two decimal places.

### 7.3 Season and Career Highs tab

- Click SEASON AND CAREER HIGHS in the header.
- A scope dropdown labelled career appears above the table. Click to choose career or season.
- Table columns: Stat Name, Value, Rank, Next Rank Value.
- Filters: Select Category, Select Substat.
- Click headers to sort; click x to clear filters.

### 7.4 Player Game Log tab

- Click PLAYER GAME LOG in the header.
- Table columns: Season, Game Date, Opponent Team Name, and stat column.
- The TOTAL row sits below the headings and updates as filters and page size change.
- Filters: Select Season, Select Category, Select Substat.
- Scroll down for page size controls — change rows per page; the table and TOTAL row recalculate.
- Click headers to sort.

### 7.5 Player Streaks tab

- Click PLAYER STREAKS in the header.
- The page shows:
- An Export button at the top-left of the table.
- A Filters section on the left with: Category, Stat, Stat Value, Streak Length, Date Range.
- A View Results button below the filters.
- To run a streak query:
- Click Select Category and choose a category.
- Click Select Stat and choose a stat.
- Click into Stat Value and type a numeric threshold.
- Click into Streak Length and type the minimum streak length.
- (Optional) Pick a Date Range to bound the streak window.
- Click View Results — the table reloads with matching streaks.
- To change the threshold, edit Stat Value and click View Results again.
- To remove date range, click x next to the selected dates.
- Click Export to download the current streak table as Excel.

### Returning to the dashboard

Click the Athlyte logo (top-left) or open the profile dropdown → Dashboard.

## 8. Team Dashboard

The Team Dashboard shows a single team's full statistical profile across five tabs.

#### Step-by-Step Navigation

1. Search for a query (e.g., `teams with more than 30 points in a game`).
2. From the results table, click the hyperlinked team name in the TEAM column to open that team's dashboard.
3. Click TEAM STATISTICS to view the team's aggregate stats by season.
4. Click TEAM RECORDS to view the team's performance records with rankings, game dates, and opponents.
5. Click SEASON HIGHS to view the highest value the team recorded for each stat within a season.
6. Click TEAM GAME LOGS to view a game-by-game list of results, scores, and stats.
7. Click TEAM STREAKS to query consecutive-game streaks for any stat threshold.

### Tab navigation (top of body)

Five primary action buttons:

- TEAM STATISTICS
- TEAM RECORDS
- SEASON HIGHS
- TEAM GAME LOGS
- TEAM STREAKS

Click any button to switch tabs; the body updates to the corresponding panel.

### 8.1 Team Statistics tab

Displays an overview of the team's seasonal statistics, with aggregate values available for every season.

- Click TEAM STATISTICS in the header.
- The body shows a table of aggregate stats per season.
- Filter the data using three dropdowns at the top of the table:
- Select Season — limit results to one or more seasons.
- Select Category — pick a stat category (e.g. Passing, Rushing).
- Select Substat — pick specific stats within the category. Multi-select supported.
- Click any column header to sort.
- To clear a selection, click the x next to the selected value.

### 8.2 Team Records tab

Details the team's performance records, including the stat name, value, rank, the stat value of the rank above, game date, and opponent team.

- Click TEAM RECORDS in the header.
- Filters: Select Period, Select Season, Select Category, Select Substat.
- Table columns: Stat Name, Value, Rank, Next Rank Value, Game Date, Opponent Team.
- Click a dropdown to expand options; tick a value to filter; click x to remove.
- Click any column header to sort.
- Decimal values are rounded to two decimal places.

### 8.3 Season Highs tab

Displays the highest value achieved by the team for each statistic within a season, along with the game date on which it was recorded.

- Click SEASON HIGHS in the header.
- Filters: Select Season, Select Category, Select Substat.
- Table columns: Stat Name, Value, Game Date.
- Apply filters via the dropdowns; click x to clear.
- Click any column header to sort.

### 8.4 Team Game Logs tab

Lists every game played by the team in a season, including the opposing team, result, and score.

- Click TEAM GAME LOGS in the header.
- Filters: Select Season, Select Category, Select Substat.
- Table columns: Game Date, Opponent Team, Result, Score, plus stat columns based on filters.
- Scroll down for page size controls — change rows per page; the table recalculates.
- Apply filters via the dropdowns; click x to clear.
- Click any column header to sort.

### 8.5 Team Streaks tab

Provides information on the team's statistical performance across consecutive games for all stats.

- Click TEAM STREAKS in the header.
- The page shows:
- An Export button at the top-left of the table.
- A Filters section on the left with: Category, Stat, Stat Value, Streak Length, Date Range.
- A View Results button below the filters.
- To run a streak query:
- Click Select Category and choose a category.
- Click Select Stat and choose a stat.
- Click into Stat Value and type a numeric threshold.
- Click into Streak Length and type the minimum streak length.
- (Optional) Pick a Date Range to bound the streak window.
- Click View Results — the table reloads with matching streaks.
- To change the threshold, edit Stat Value and click View Results again.
- To remove the date range, click x next to the selected dates.
- Click Export to download the current streak table as Excel.

### Returning to the dashboard

Click the Athlyte logo (top-left) or open the profile dropdown → Dashboard.

## 9. Search Information Centre (Help)

This is the help page that helps the user to navigate through the application's features. It has everything in detail about the following:

- Login Page
- Search Dashboard
- How to Search
- Export Data
- Report an Issue
- Data Centre
- Records

Click any tile to open its detail page.

### 9.1 Login Page tile

Documents the three-step login (Username, Password, Login button), shows a screenshot of the login form, walks through Sign Up via Outlook, and explains the Forgot Password / Send Reset Link flow with a sample reset email.

### 9.2 Search Dashboard tile

Describes the natural-language search tool. Explains the Player vs Team toggle. Shows screenshots of the dashboard, results table, Export Data button, and the filter panel. A Click here link points to the Query Builder guide.

### 9.3 How to Search tile

Documents the five query categories — Basic, Complex, Records, Last Time, Streaks — with checkmarks for which support Qualifiers and Periods, and example queries for each. Notes:

- A sport must be selected before starting a query.
- Valid periods are Game, Season, Career.
- Career is available for Player stats only — not Team stats.
- Adding qualifiers is optional; multiple qualifiers can be combined.

### 9.4 Export Data tile

Step-by-step:

- Run a search.
- On the Result Screen, click Export at the top of the table.
- A .xlsx file downloads containing the same rows shown in the table (filters applied).

### 9.5 Report an Issue tile

Step-by-step:

- Click the Report Issue button at the top-right of the Dashboard or Result Screen.
- A pop-up window opens with a description text area.
- Type details of the bug in the description box.
- Submit — the report is sent to the admin for resolution.

### 9.6 Data Centre tile

Anchor links jump to per-sport sections (Men's Football, Men's Basketball, Women's Basketball). Each section contains tables with the schema: Name | Category | Sub-category | Description | Availability.

Use this page to look up the definition of any stat exposed in the search bar.

### 9.7 Records Book

Shows the record book data available on search for the team.

## 10. Plans & Upgrade Flow

Reached by:

- Clicking the Upgrade button in the top-right corner of the screen.
- Navigating from the Profile page (username dropdown → Profile → upgrade options).

The upgrade flow is a multi-step wizard: Select Sport → Choose Add-ons → Checkout.

### Step 1 — Select a Sport

- Click the sport you want to subscribe to from the list of available sports.
- Click Continue to advance to the add-ons page.

### Step 2 — Choose Add-ons

On the add-ons page you can customise your subscription in two ways:

Option A — Buy the sport with add-ons

- Review the available add-ons for the selected sport.
- Tick the add-ons you want to include.
- Click Continue to Checkout.

Option B — Buy only the sport (no add-ons)

- Tick the Enable checkbox on each add-on to disable it. The Enable checkbox acts as a toggle — checking it removes the add-on from your order.
- Once all add-ons are disabled, click Continue to Checkout.

### Step 3 — Review Order Summary

On the checkout page, the Order Summary panel reflects the correct total based on the sport and add-ons selected.

| Action | How |
| --- | --- |
| Add more sports | Click + Add more sports to return to the sport-selection page and include another sport in the same order. |
| Pay by card | Click Proceed to Payment to pay immediately via Stripe. |
| Pay by invoice | Choose the invoice option to generate a Stripe invoice and gain temporary grace access while the invoice is outstanding. |

Verify the line items and the final total in the Order Summary match your selection before proceeding. If anything looks off, go back and adjust add-ons first.

### Existing-subscriber behaviour

- The Profile page (username dropdown → Profile) shows the current subscription plan, active sports, and options to upgrade (add new sports or add-ons).
- From the Dashboard, the Change Plan button returns the user to the same plan-selection page to adjust their subscription.

## 11. Checkout Flow

Trigger: clicking Continue to Checkout on the add-ons page, or Proceed to Payment / the invoice option from the Order Summary.

### Layout

The checkout page displays an Order Summary panel on the right (desktop) or below (mobile) showing all selected sports and add-ons with the final total. A +Add more sports  lets the user return to sport selection before paying.

### Option 1 — Pay Directly by Card

- Confirm the Order Summary line items and total match your selection.
- Click Proceed to Payment. You are redirected to a secure Stripe payment page.
- Enter your card details on Stripe and complete the transaction.
- Wait for Stripe to confirm the payment.

If payment succeeds:

- You are redirected automatically to the search page.
- An on-screen confirmation message confirms that your subscription is active.

If payment fails:

- You will be directed to the Payment Pending page.
- Review your order, then either go back to check out or change the plan and complete the payment.

### Option 2 — Generate an Invoice (Grace Access)

- On the checkout page, choose the invoice option instead of Proceed to Payment.
- The system generates a Stripe invoice and refreshes your session so that grace access is applied to your account immediately.
- Pay the invoice within the grace period to maintain uninterrupted access.

Grace access: Lets you start using your subscription immediately while the Stripe invoice is still outstanding. Settle the invoice before the grace period ends to avoid losing access.

## 12. Common UI Elements

These elements appear consistently across multiple pages.

### 12.1 Header (every authenticated page)

- Athlyte logo (top-left) — clicking it always returns to Dashboard.
- Team logo — appears next to the Athlyte logo on Game/Player/Result pages.
- Sport switcher — Football / Basketball/ Ice Hockey/ Soccer/ Volleyball.
- Help icon ? — opens the Search Information Centre.
- Profile dropdown (top-right) — Username (display), Dashboard (link), Sign out (link).

### 12.2 Footer (every page)

Reads: Athlyte College Sports Communicator © 2025 Athlyte. All Rights Reserved. Default. Scroll to the bottom of any page to see it.

### 12.3 Trial banner

Shown on every authenticated route during a trial.

- Text: You have N days left in your trial. (singular 1 day on the last day).
- Has a close X to dismiss for the session.
- Has an Upgrade button that routes to plans.
- Hidden for paid users; replaced by a full-screen Trial Ended overlay once the 14-day trial expires.

### 12.4 Graphics and Charts (Visualize Data panel)

Available on Search Result Screens after a query returns at least one row.

#### Step-by-step

- Run a search and confirm the results table is displayed.
- Click Visualize Data on the top right side of the table.
- The chart panel opens (side panel on desktop, stacked panel on mobile). The chart type depends on the query category.
- Click the chart's close button to dismiss the panel — the table layout returns to its original state.

#### Empty / error states

- Empty — clear message "No chart data available".
- Error — friendly fallback message with a Retry button. Retry refetches and renders if the error is transient.

### 12.6 Report Issue modal

- Click the Report Issue button (typically top-right of Dashboard / Result Screen).
- A pop-up window opens with a description text area.
- Type the bug details.
- Click Submit — the report is delivered to the admin team.
- Close the pop-up to return to the page you were on.

## Appendix — End-to-end smoke flow

The shortest path that exercises every primary page:

- Go to Login, enter credentials, click Login.
- Dismiss the onboarding wizard if it appears.
- On Dashboard, switch to Football, ensure the Player toggle is active.
- Type Players with points per game > 20 into the search bar and press Enter.
- On the Result Screen, click a column header to sort, apply an Opponent Conference filter, and click Export.
- Click a player's name to open their Player Dashboard.
- Click PLAYER STATISTICS, then PLAYER RECORDS → season, then PLAYER STREAKS and run a streak query.
- Click the Athlyte logo to return to the Dashboard.
- Click an Upcoming Game card to open the Game Dashboard.
- Click the ? help icon to open the Search Information Centre, browse a tile, then click the Back arrow.
- Open the profile dropdown → Sign out to return to Login.
