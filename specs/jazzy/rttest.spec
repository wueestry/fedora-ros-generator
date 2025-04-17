# Meta Package
Name:           ros-jazzy-rttest
Version:        0.17.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-rttest and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rttest
Requires:       ros2-jazzy-rttest-devel

Obsoletes: ros-jazzy-rttest < 0.17.1-1

%description
Instrumentation library for real-time performance testing

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 05 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.17.1-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.17.0-1
- Update to latest release
