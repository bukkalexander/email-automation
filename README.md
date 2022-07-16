# Fika Script
## user story
- There is a list of people who will take turns to bring fika each week
- In the start of every week, one person is appointed as responsible to bring fika at a specific weekday time.
- Everyone should get a calendar invitation in the beginning of the week, which states a `place`, `datetime` and `responsible` for fika
- In the start of the week, and the day before the fika `datetime`, the `resonsible` is reminded to bring fika.
- Next week, the list is modified, so that the `responsible` is added to the bottom of the fika list.
- Then, all the previous actions are repeated

## Design
- schedule job 1 on mondays which sends out invitation and email to responsible person
- schedule job 2 which sends out an email reminder, and then modifies the fika list and puts the last responsible in the bottom

## Implementation
- job 1: call fika_script invitation reminder
- job 2:call fika_script reminder rotate

## TODO
- create methods:
  - send_invitation
  - send_reminder
  - rotate_list