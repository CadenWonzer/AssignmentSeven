"""
Student information for this assignment:

Replace <FULL NAME> with your name.
On my/our honor, Caden Wonzer and Isabella Chojnacki, this
programming assignment is my own work and I have not provided this code to
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1: czw99
UT EID 2: ilc422
"""


class Node:
    """
    A modified version of the Node class for linked lists (using proper class
    coding practices). Instead of a data instance variable, this node class has both
    a coefficient and an exponent instance variable, which is used to represent each
    term in a polynomial.
    """

    def __init__(self, coeff, exp, link=None):
        """
        Node Constructor for polynomial linked lists.

        Args:
        - coeff: The coefficient of the term.
        - exp: The exponent of the term.
        - link: The next node in the linked list.
        """
        self.coeff = coeff
        self.exp = exp
        self.next = link

    @property
    def coeff(self):
        """
        Getter method for the coefficient attribute.
        """
        return self.__coeff

    @coeff.setter
    def coeff(self, value):
        """
        Setter method for the coefficient attribute.
        """
        if value is None or isinstance(value, int):
            self.__coeff = value
        else:
            raise ValueError("Coefficient must be an integer or None.")

    @property
    def exp(self):
        """
        Getter method for the exponent attribute.
        """
        return self.__exp

    @exp.setter
    def exp(self, value):
        """
        Setter method for the exponent attribute.
        """
        if value is None or isinstance(value, int):
            self.__exp = value
        else:
            raise ValueError("Exponent must be an integer or None.")

    @property
    def next(self):
        """
        Getter method for the next attribute.
        """
        return self.__next

    @next.setter
    def next(self, value):
        """
        Setter method for the next attribute.
        """
        if value is None or isinstance(value, Node):
            self.__next = value
        else:
            raise ValueError("Next must be a Node instance or None.")

    def __str__(self):
        """
        String representation of each term in a polynomial linked list.
        """
        return f"({self.coeff}, {self.exp})"


class LinkedList:
    def __init__(self):
        # You are also welcome to use a sentinel/dummy node!
        # It is definitely recommended, which will we learn more
        # about in class on Monday 10/21. If you choose to use
        # a dummy node, you can comment out the self.head = None
        # and comment in the below line. We use None to make sure
        # if there is an error where you accidentally include the
        # dummy node in your calculation, it will throw an error.
        # self.dummy = Node(None, None)
        self.head = None

    # Insert the term with the coefficient coeff and exponent exp into the polynomial.
    # If a term with that exponent already exists, add the coefficients together.
    # You must keep the terms in descending order by exponent.
    def insert_term(self, coeff, exp):
        if coeff == 0:
            return
        new_node = Node(coeff, exp)
        if not self.head or self.head.exp < exp:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        previous = None
        while current and current.exp > exp:
            previous = current
            current = current.next
        if current and current.exp == exp:
            current.coeff += coeff
            if current.coeff == 0:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
            return
        new_node.next = current
        if previous:
            previous.next = new_node
        else:
            self.head = new_node

    # Add a polynomial p to the polynomial and return the resulting polynomial as a new linked list.
    def add(self, p):
        result = LinkedList()
        p1 = self.head
        p2 = p.head
        while p1 or p2:
            if p1 and (not p2 or p1.exp > p2.exp):
                result.insert_term(p1.coeff, p1.exp)
                p1 = p1.next
            elif p2 and (not p1 or p1.exp < p2.exp):
                result.insert_term(p2.coeff, p2.exp)
                p2 = p2.next
            else:
                added_coeff = p1.coeff + p2.coeff
                if added_coeff != 0:
                    result.insert_term(added_coeff, p1.exp)
                p1 = p1.next
                p2 = p2.next
        return result

    # Multiply a polynomial p with the polynomial and return the product as a new linked list.
    def mult(self, p):
        result = LinkedList()
        self_current = self.head
        p_current = p.head
        while self_current is not None:
            while p_current is not None:
                if result.head == None:
                    result.head = Node(self.coeff * p.coeff, self.exp + self.exp)

    # Return a string representation of the polynomial.
    def __str__(self):
        output = ""
        coeff_list = []
        exp_list = []
        current = self.head
        
        while current is not None:
            coeff_list.append(current.coeff)
            exp_list.append(current.exp)
            current = current.next
        
        for i in range(len(coeff_list)):
            term = (coeff_list[i], exp_list[i])
            output += str(term)
            if i != len(coeff_list) - 1:
                output += " + "
            else:
                break
        
        return output


def main():
    # read data from stdin using input() and create polynomial p

    # read data from stdin using input() and create polynomial q

    # get sum of p and q as a new linked list and print sum

    # get product of p and q as a new linked list and print product
    
    p = LinkedList()
    p_terms = int(input())
    last_node = None

    for _ in range(p_terms):
        term_str = input().strip().split()
        if p.head is None:
            p.head = Node(int(term_str[0]), int(term_str[1]))
            last_node = p.head
        else:
            last_node.next = Node(int(term_str[0]), int(term_str[1]))
            last_node = last_node.next
            
    input()
    
    q = LinkedList()
    q_terms = int(input())
    last_node = None

    for _ in range(q_terms):
        term_str = input().strip().split()
        if q.head is None:
            q.head = Node(int(term_str[0]), int(term_str[1]))
            last_node = q.head
        else:
            last_node.next = Node(int(term_str[0]), int(term_str[1]))
            last_node = last_node.next
     
    print(p)
    print(q)     
    p.add(q) 


if __name__ == "__main__":
    main()
