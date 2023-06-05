from tkinter import *
from tkinter import ttk

class ToggleAllCheckbutton(ttk.Checkbutton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.checkbox_variables: list[IntVar] = []
        self.value = IntVar(value=1)

        self.configure(variable=self.value, command=self.set_children_checkbox_states)
    
    def set_children_checkbox_states(self):
        for variable in self.checkbox_variables:
            variable.set(self.value.get())

    def add_child_checkbox(self, checkbox_variable: IntVar):
        self.checkbox_variables.append(checkbox_variable)
        checkbox_variable.trace_add("write", self.child_checkbox_changed_state)

    def child_checkbox_changed_state(self, *args):
        all_variables_true = True
        all_variables_false = True

        for variable in self.checkbox_variables:
            if variable.get() == True:
                all_variables_false = False

            if variable.get() == False:
                all_variables_true = False
        
        if all_variables_false:
            self.value.set(False)
            return
        
        if all_variables_true:
            self.value.set(True)
            return
        
        self.state(["alternate"])
