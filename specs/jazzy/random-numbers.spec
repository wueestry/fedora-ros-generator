# Meta Package
Name:           ros-jazzy-random-numbers
Version:        2.0.1
Release:        1%{?dist}
License:        BSD
URL:            http://ros.org/wiki/random_numbers
Summary:        Meta package for ros2-jazzy-random_numbers and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-random_numbers
Requires:       ros2-jazzy-random_numbers-devel

Obsoletes: ros-jazzy-random-numbers < 2.0.1-1

%description
This library contains wrappers for generating floating point values,
integers, quaternions using boost libraries. The constructor of the
wrapper is guaranteed to be thread safe and initialize its random
number generator to a random seed. Seeds are obtained using a separate
and different random number generator.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.0.1-1
- Update to latest release
