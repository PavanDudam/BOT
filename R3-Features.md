# R3 Features Overview

This document outlines the key features introduced in the R3 (Release 3) version of the Athlyte Search platform. These features enhance the user experience by providing improved data visualization, advanced search assistance, detailed game insights, and expanded sports coverage.

The R3 features include:

- Play-by-Play in Game Dashboard
- Team Dashboard (Team Statistics, Team Records, Season Highs, Team Game Logs, Team Streaks)
- Typeahead search suggestions for faster query input
- Visualize Data functionality for charts and graphical insights
- Ask Athlyte assistant for guided querying and platform help
- Enhanced payment and subscription workflow
- Support for new sports including Ice Hockey, Soccer, and Volleyball

Each section below explains these features in detail.

## Game Dashboard

The game dashboard has detailed insights about the game which include: Player Stats, Team Stats, Roster and Play-by-Play information of the game.

### Player Stats

Provides a detailed breakdown of individual player statistics for both teams in the game.

Filters: A "Category:" dropdown allows users to change the type of statistics displayed (e.g., passing, rushing, receiving, etc.).

### Team Stats

It provides a side-by-side comparison of various statistical categories for both team and opponent team for the specified game.

### Rosters

The "Rosters" tab of the game dashboard provides a list of players for both competing teams during this specific game.

### Play-by-Play

This gives a detailed description of every action, movement, and event of a match as it unfolds.

Filters: A "Show" dropdown allows users to filter the roster between starters and the full roster.

## Team Dashboard

### Team Statistics

The "Team Statistics" section of a team's dashboard offers an overview of the seasonal stats of the team. The aggregate statistics for every season can be viewed.

Filters: These stats can be filtered based on season, stat category, and substat.

### Team Records

This page details a team's performance, including the stat name, value, rank, and the stat value of the rank above. It also displays the game date for each statistic and the opponent's team.

Filters: These stats can be filtered based on period, season, stat category, and substat.

### Season Highs

Displays the highest value achieved by the team for each statistic in a season, as well as the game date on which it was recorded.

Filters: These stats can be filtered based on season, stat category, and substat.

### Team Game Logs

Gives a complete list of all games played by the team in a season, including the opposing team, result, and score for each game.

Filters: These stats can be filtered based on season, stat category, and substat.

### Team Streaks

Team Streaks provides information on a team's statistical performance for all stats across consecutive games.

## Typeahead

The feature adds real-time autocomplete to the existing search experience. As a user types into the search box, a dropdown appears beneath it showing matching suggestions they can pick from instead of typing the full query.

## Visualize Data

The "Visualize Data" feature adds simple visual representations to search results. After performing a search, users can click the "Visualize Data" button near the results table to display a chart based on the selected query and relevant period (game or season).

The type of queries supported for this are:

- Simple
- Complex
- Records
- Last Time When
- Streaks

**Simple:** For basic queries (e.g., "players with rushing yards > 50"), a horizontal bar chart shows the top 10 players who met the condition the most number of times. No. of occurrences shows how often each player achieved the stat.

**Complex:** For queries with more than one condition (e.g., "players with rushing yards > 50 and passing yards > 10"), a scatter plot shows the top 10 players who met both conditions most frequently.

**Records (Min & Max):** For record-based queries (e.g., "highest rushing yards in a game"), a line chart takes the first 10 entries from the results table (even if the same player appears more than once) and plots each player's record game in the center, with up to 3 games before and 3 games after.

**Last Time When:** In last time when queries, a line chart picks the unique players from the results and plots up to 10 of their games.

**Streaks:** For queries tracking consecutive-game performance (e.g., "players with > 50 rushing yards in consecutive games"), a line chart plots the stat value across each game in the streak, with the streak length indicated next to each player's name.

## Ask Athlyte

The Ask Athlyte Bot is a sports analytics assistant integrated into the platform. It helps users explore stats, frame sports queries effectively to get the best results from the Athlyte search feature, and answer any questions about how to use the platform.

## Payment Process

This guide walks you through how to upgrade your subscription, choose a sport, add or remove add-ons, complete checkout (either by card or invoice), and manage your profile. Follow the steps in order — each section builds on the previous one.

### 1. Starting the Upgrade Flow

- Locate the Upgrade button in the top-right corner of the screen.
- Click Upgrade. The plan-selection page will open.

### 2. Selecting a Sport

- From the list of available sports, click on the one you want to subscribe to.
- Click Continue to move forward to the add-ons page.

### 3. Choosing Add-ons (or Skipping Them)

On the add-ons page, you can customise your subscription in two ways:

**Option A — Buy the sport with add-ons**

- Review the available add-ons for the sport you selected.
- Tick the add-ons you want to include in your subscription.
- Click Continue to Checkout.

**Option B — Buy only the sport (no add-ons)**

- Tick the Enable checkbox on each add-on to disable them.
- Once all add-ons are disabled, click Continue to Checkout.

Note: The Enable checkbox acts as a toggle — checking it removes the add-on from your order so you only pay for the sport itself.

### 4. Reviewing Your Order Summary

On the checkout page, the Order Summary panel should reflect the correct total based on the sport and add-ons you selected.

What you can do from here:

- Add more sports: click the +Add more sports CTA to return to the sport-selection page and include another sport in the same order.
- Proceed to payment: pay immediately by card via Stripe.
- Generate an invoice: receive a Stripe invoice and gain temporary (grace) access while payment is pending.

Check before paying: Verify the line items and the final total in the Order Summary match your selection. If anything looks off, go back and adjust your add-ons before proceeding.

### 5. Completing Payment

**Option 1 — Pay Directly**

- Click Proceed to Payment. You will be redirected to a secure Stripe payment page.
- Enter your card details and complete the transaction on Stripe.
- Wait for Stripe to confirm the payment.

If payment is successful:

- You will be redirected to the search page automatically.
- A confirmation message will appear on-screen verifying that your subscription is active.

If payment fails:

- You will be directed to the Payment Pending page.
- Review your order, then either choose “Back to Checkout” or “Change Plan” instead.

**Option 2 — Generate an Invoice**

- Choose the invoice option at checkout instead of Proceed to Payment.
- The system will generate a Stripe invoice and refresh your session so that grace access is applied to your account.
- Pay the invoice within the grace period to keep uninterrupted access.

Grace access: Grace access lets you start using your subscription immediately while the invoice is still outstanding. Make sure to settle the invoice before the grace period ends to avoid losing access.

### 6. Managing Your Profile

Your profile is the dashboard where you can review and manage your account.

How to access your profile:

- Click on your username in the top-right corner.
- Select Profile from the dropdown menu.

What you'll see:

- Your account details and subscription plan.
- View your account details (username, email, designation, full name) along with your current subscription plan (e.g., Premium) and a cost breakdown for Sports, Add-ons, and Total.
- Subscribed Sports: See all sports you're subscribed to, along with their access expiry dates. Click Add a Sport to subscribe to a new one.
- Active Add-ons: View any add-ons currently active on your account. Click Add more to purchase additional add-ons.

Step-by-step navigation:

1. Click on Username (top-right corner)
2. Open the Dropdown menu
3. Select Profile
4. On the Profile page, view Account Details & Plan, Subscribed Sports, and Active Add-ons
   - Click “Add a Sport” to subscribe to a new sport
   - Click “Add more” to purchase additional add-ons

Quick reference:

- Start: Top-right Upgrade button.
- Pick: Sport → Add-ons (toggle Enable checkbox to drop them) → Continue.
- Review: Order Summary must match your selection.
- Pay: Proceed to Payment (Stripe) OR Generate Invoice (grace access).
- Success: Redirect to search page + on-screen confirmation.
- Failure: Sent back to Checkout.
- Manage: Username dropdown → Profile to view or change your plan.

## New Sports

These sports have been added to the new release of search:

- Men’s Ice Hockey
- Women’s Ice Hockey
- Men’s Soccer
- Women’s Soccer
- Men’s Volleyball
- Women’s Volleyball

## All Sports

These are all the sports the search platform supports currently:

- Men’s Football
- Men’s Basketball
- Women’s Basketball
- Men’s Ice Hockey
- Women’s Ice Hockey
- Men’s Soccer
- Women’s Soccer
- Men’s Volleyball
- Women’s Volleyball
