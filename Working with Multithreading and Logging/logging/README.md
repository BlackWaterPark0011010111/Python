

# Logger
                +--------------------------------+
                | Logging call in user code     |
                | e.g., logger.info(...)        |
                +--------------------------------+
                               |
                               v
                +--------------------------------+
                | Logger enabled for level?      |
                +--------------------------------+
                     | Yes             | No
                     v                 v
    +-----------------------------+     Stop
    | Create LogRecord            |
    +-----------------------------+
                     |
                     v
    +---------------------------------------------+
    | Does a filter attached to logger reject it? |
    +---------------------------------------------+
                     | Yes             | No
                     v                 v
                    Stop      +-------------------------------+
                              | Pass record to handlers       |
                              +-------------------------------+
                                               |
                                               v
    +----------------------------------------------+
    | Is propagate true for the current logger?   |
    +----------------------------------------------+
                     | Yes             | No
                     v                 v
    +---------------------------------+   +------------------+
    | Is there a parent logger?       |   | Check handlers   |
    +---------------------------------+   +------------------+
        | Yes            | No                       |
        |                |                          |
        v      
                         v            
                                                    v

  +------------------+   Stop          +----------------------------------+
  | Set logger to    |                 | Is there at least one handler? |
  | parent logger    |                 +----------------------------------+
  +------------------+                   | Yes            | No
        |                                 v                v
        |                       +-------------------------------+
        |                       | Pass record to handlers       |
        |                       +-------------------------------+
        |                                 |
        |                                 |
        |                                 v
  +------------------+     +----------------------------------+
  | Parent logger?   |     | Use lastResort handler         |
  +------------------+     +----------------------------------+
        | Yes
        v
  (Back to checking propagation)

                           ** Handler flow **
    +--------------------------------------------+
    | Record passed to handler                   |
    +--------------------------------------------+
                     |
                     v
    +----------------------------------------+
    | Handler enabled for level of record?  |
    +----------------------------------------+
                     | Yes             | No
                     v                 v
    +---------------------------------+   Stop
    | Does a filter reject the record? |
    +---------------------------------+
                     | Yes             | No
                     v                 v
                    Stop       +----------------------+
                               | Emit (includes formatting) |
                               +----------------------+
        

