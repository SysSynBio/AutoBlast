def show_time(process, time_start, time_end):
    time_took = str(process) + " finished in "
    if (round((time_end-time_start)/60, 1) < 1):
      time_took = time_took + str(round((time_end-time_start), 2)) + " seconds "
    elif (round((time_end-time_start)/60/60, 1) < 1):
      time_took = time_took + str(round((time_end-time_start)/60, 2)) + " minutes "
    else:
      time_took = time_took + str(round((time_end-time_start)/60/60, 1)) + " hours "
    time_took = time_took + " (wallclock)."
    return time_took
############### end of show_time function
