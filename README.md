Question 1: By default are django signals executed synchronously or asynchronously? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

Answer: 
By default, Django signals are executed synchronously. When a signal is sent, the receiver functions connected to that signal are executed in the same thread, blocking the execution until all the receiver functions finish. If we want to handle signals asynchronously, we would need to implement that manually by using threading, background tasks, or Django's built-in async features (like asgiref for async consumers).
