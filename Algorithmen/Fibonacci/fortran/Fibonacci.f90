program fibonacci
    implicit none
    
    !boilerplate
    integer :: n, m, iterations, i
    integer(kind=8) :: fib

    !input
    write(*,*) "Enter the first number"
    read(*,*) n

    write(*,*) "Enter the second number"
    read(*,*) m

    write(*,*) "Enter the number of iterations"
    read(*,*) iterations

    !calculation

    i = 0
    do while (i < iterations)
        fib = n + m
        n = m
        m = fib
        i = i + 1

        if (fib < 0) then
            write(*,*) "Integer Overflow"
            exit
        end if

        write(*,*) i, fib
    end do

end program fibonacci