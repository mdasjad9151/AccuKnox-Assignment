<h1>Django Signals</h1>

**Question 1:** By default are django signals executed synchronously or asynchronously? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

**Answer:**
By default, Django signals are executed synchronously. When a signal is sent, the receiver functions connected to that signal are executed in the same thread, blocking the execution until all the receiver functions finish. If we want to handle signals asynchronously, we would need to implement that manually by using threading or Celery.

1. For an example of synchronous signal, I named my app _'question1'_. When we hit the _'/question1/'_ URL, we will notice a 10-second delay in the views page (the first 5 seconds from pre-signle and the second 5 seconds from post-signal) due to a single block of activity.

**Code directory**: signals/question2/signals.py.
**Test**:- /question1/

2. On the other hand, I created anynchronus single applying threading in my _'question1Async'_ app; when we hit the _'/quetion1Async/'_ url, we will see no dealy, but the signal will complete all of its operations after 5 seconds, as I mentioned in the delay time.

**Code directory:** signals/question1Async/signals.py.
**Test:** /question1Async/.

**Question 2:** Do django signals run in the same thread as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

**Answer:**
Yes, Django signals run in the same thread as the caller by default. This means that when a signal is emitted (for example, when saving a model and triggering the post_save signal), the receiver functions are executed synchronously in the same thread. As a result, the signal processing will block further execution until all connected receiver functions have completed their work.

For an example of same thread signal, I named my app 'question2'.When we access the view that creates a new User, the post_save signal is triggered. The signal handler (_post_handler_) runs in the same thread, and during the 5-second time.sleep, the entire request is blocked, meaning the response to the user is delayed until the signal has completed.This behavior confirms that Django signals run in the same thread as the caller.

**Code directory:**:- signals/question2/signals.py
**Test:-** /question2/

**Question 3:** By default do django signals run in the same database transaction as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

**Answer:-**
By default, Django signals do not automatically run in the same database transaction as the caller. However, there are specific signals, like pre_save and post_save, that are emitted during certain stages of model saving and updating. Their behavior with transactions depends on when they are emitted in relation to the database operations.
If we need a signal handler to run only after a successful database commit, we can use _transaction.on_commit()_ in Django. This ensures that the code in the signal handler runs only after the transaction is committed.

**code dir:-** signals/question3/signals.py
**test:-** /question3/

<h1>Custom Classes in Python</h1>

**Question :-** Description: You are tasked with creating a Rectangle class with the following requirements:

1. An instance of the Rectangle class requires length:int and width:int to beinitialized.
2. We can iterate over an instance of the Rectangle class
3. When an instance of the Rectangle class is iterated over, we first get its length in theformat: {'length': <VALUE_OF_LENGTH>} followed by the width {width:<VALUE_OF_WIDTH>}

**Answer:-** code dir: - signals/oops/Q1.py
