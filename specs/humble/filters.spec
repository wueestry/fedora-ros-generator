# Meta Package
Name:           ros-humble-filters
Version:        2.1.0
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-filters and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-filters
Requires:       ros2-humble-filters-devel

Obsoletes: ros-humble-filters < 2.1.0-1

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
* Sat Oct 21 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.1.0-1
- update to latest release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - noetic.1.9.2-1
- update to latest release
