# Meta Package
Name:           ros-humble-rttest
Version:        0.13.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-rttest and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-rttest
Requires:       ros2-humble-rttest-devel

Obsoletes: ros-humble-rttest < 0.13.0-1

%description
Instrumentation library for real-time performance testing

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.13.0-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.13.0-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.13.0-1
- Initial humble build
