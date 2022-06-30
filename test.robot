*** Settings ***
Resource   common.resource

*** Test Cases ***
Device Sends App Data
  [Documentation]     Tests if appdata is as expected
  [Tags]              embedded hardware   application
  ${is_up}=           Is AppServer Up
  Should Be True      ${is_up}
