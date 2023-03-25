program three_x_plus_one
  implicit none

  !boilerplate
  integer(kind=8) :: n, count, i
  integer :: start_time, elapsed_time
  integer :: percent
  
  !prompt user for input
  write(*, *) "Enter a number:"
  read(*, *) n

  i = n
  count = 0
  call system_clock(start_time)

  !calculate
  do while (i /= 1)
    count = count + 1
    if (mod(i, 2) == 0) then
      i = i / 2
    else
      i = 3 * i + 1
    end if
  end do

  !print result
  call system_clock(elapsed_time)
  elapsed_time = (elapsed_time - start_time) * 1000
  write(*, *) "Starting number: ", n
  write(*, *) "Number of iterations: ", count
  write(*, *) "Execution time: ", elapsed_time, "ms"

end program three_x_plus_one
