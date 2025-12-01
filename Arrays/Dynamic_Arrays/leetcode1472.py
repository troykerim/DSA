'''

Leetcode 1472 - Design Browser History

You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history number of steps or move forward in the history number of steps.

Implement the BrowserHistory class:

    BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
    void visit(string url) Visits url from the current page. It clears up all the forward history.
    string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. Return the current url after moving back in history at most steps.
    string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.


This solution uses a stack/array
'''
class BrowserHistory(object):
    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.i = 0
        self.len = 1 
        self.history = [homepage]

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        if len(self.history) < self.i + 2:
            self.history.append(url)
        else:
            self.history[self.i + 1] = url
        self.i += 1 
        self.len = self.i + 1 
		
    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        self.i = max(self.i - steps, 0)
        return self.history[self.i]
        
    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        self.i = min(self.i + steps, self.len - 1)
        return self.history[self.i]