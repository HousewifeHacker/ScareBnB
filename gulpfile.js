var gulp = require('gulp');
var browserify = require('browserify')
var babelify = require('babelify');
var source = require('vinyl-source-stream');
var eslint = require('gulp-eslint');

gulp.task('build', function() {
    return browserify({entries: './app.jsx', extensions: ['.jsx'], debug: true})
        .transform(babelify)
        .bundle()
        .pipe(source('bundle.js'))
        .pipe(gulp.dest('dist'));
})

gulp.task('lint', function() {
    return gulp.src(['*.jsx'])
	// useEslintrc directs to config options eslintrc
        .pipe(eslint({
            useEslintrc: true
        }))
        // eslint.format() outputs the lint results to the console.
        .pipe(eslint.format())
        .pipe(eslint.failOnError());
});

gulp.task('default', ['build', 'lint']);
