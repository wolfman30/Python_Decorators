def log_message(func):

      def write_to_decorator_log(func):
            with open('/tmp/decorator_logs.txt', 'w+') as decorator_log: 
                  decorator_log.write(func)
      return write_to_decorator_log


@log_message

def a_function_that_returns_a_string():

      return "A string"

@log_message

def a_function_that_returns_a_string_with_newline(s):

      return "{}\n".format(s)

@log_message

def a_function_that_returns_another_string(string=""):

            return "Another string"