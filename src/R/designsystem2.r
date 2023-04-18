summary.linmod <- function(object, ...)
{
    se <- sqrt(diag(object$vcov))
    tval <- coef(object) / se
    TAB <- cbind(Estimate = coef(object),
    StdErr = se,
    t.value = tval,
    p.value = 2*pt(-abs(tval), df=object$df))
    res <- list(call=object$call,
    coefficients=TAB)
    class(res) <- "summary.linmod"
    res
}
#The utility function printCoefmat() can be used to print the matrix with appropriate rounding and some decoration:
print.summary.linmod <- function(x, ...)
{
    cat("Call:\n")
    print(x$call)
    cat("\n")
    printCoefmat(x$coefficients, P.value=TRUE, has.Pvalue=TRUE)
}
