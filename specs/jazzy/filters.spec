# Meta Package
Name:           ros-jazzy-filters
Version:        2.1.2
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-filters and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-filters
Requires:       ros2-jazzy-filters-devel

Obsoletes: ros-jazzy-filters < 2.1.2-1

%description
This library provides a standardized interface for processing data as
a sequence of filters. This package contains a base class upon which
to build specific implementations as well as an interface which
dynamically loads filters based on runtime parameters.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.1.2-1
- Update to latest release
