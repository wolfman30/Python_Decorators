def log_message(func):

      def wrapper(*args):
            with open('tmp/decorator_logs.txt', 'w+') as decorator_log: 
                  decorator_log.write(func(*args))
      
      return wrapper


@log_message
def a_function_that_returns_a_string():

      return "A string"

@log_message
def a_function_that_returns_a_string_with_newline(s):

      return "{}\n".format(s)

@log_message
def a_function_that_returns_another_string(string=""):

            return "Another string"

if __name__ == '__main__':
      a_function_that_returns_a_string()
      a_function_that_returns_a_string_with_newline('write me')
      a_function_that_returns_another_string()