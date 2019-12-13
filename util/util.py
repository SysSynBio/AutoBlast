import os

def show_header(title):
    print "\n"
    multiply_asterisk = 95
    print '#'*multiply_asterisk
    number_of_remaining_sharp = multiply_asterisk - len(title)
    put_this_number_of_sharp = int(int(number_of_remaining_sharp)/2)
    print '#'*(put_this_number_of_sharp-1) + " " + title + " " + '#'*(put_this_number_of_sharp-1)
    print '#'*multiply_asterisk
########### end of show_header function


def show_time(process, time_start, time_end):
    time_took = str(process) + " finished in "
    if (round((time_end-time_start)/60, 1) < 1):
      time_took = time_took + str(round((time_end-time_start), 1)) + " seconds "
    elif (round((time_end-time_start)/60/60, 1) < 1):
      time_took = time_took + str(round((time_end-time_start)/60, 1)) + " minutes "
    else:
      time_took = time_took + str(round((time_end-time_start)/60/60, 1)) + " hours "
    time_took = time_took + "(wallclock)."
    return time_took
############### end of show_time function
