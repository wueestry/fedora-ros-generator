# Meta Package
Name:           ros-iron-rttest
Version:        0.15.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-rttest and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rttest
Requires:       ros2-iron-rttest-devel

Obsoletes: ros-iron-rttest < 0.15.0-1

%description
Instrumentation library for real-time performance testing

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.15.0-1
- Update to latest release
