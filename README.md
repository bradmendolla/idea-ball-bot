# idea-ball-bot
Simple discord bot that pings online users within a specific role. 

## Commands
*All commands are prefixed by the standard exclamation point (!)*

#### Admin Commands
**!setup:** bot creates a role called "IdeaBall". Setup command checks and recognizes if role already exists to avoid creating additional roles with the same name.

#### User Commands
**!join:** bot adds user to the IdeaBall role.  
**!leave** bot removes user from IdeaBall role.  
**!playball:** bot randomly pings someone in the IdeaBall role who is online (excludes person who invokes command).  
**!players:** bot lists number of people online in the IdeaBall role.  

#### Miscellaneous commands  
**!claptrap:** selects a random CL4P-TP quote.   

## Permissions Required
The bot requires Manage Roles, View Channels, and Send Messages permissions.  