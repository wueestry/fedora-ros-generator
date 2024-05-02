# Meta Package
Name:           ros-humble-tinyxml2-vendor
Version:        0.7.6
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-tinyxml2_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-tinyxml2_vendor
Requires:       ros2-humble-tinyxml2_vendor-devel

Obsoletes: ros-humble-tinyxml2-vendor < 0.7.6-1

%description
Wrapper around tinyxml2, providing nothing but a dependency on
tinyxml2, on some systems. On others, it provides a fixed CMake module
or even an ExternalProject build of tinyxml2.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Dec 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.7.6-1
- update to latest upstream
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.7.5-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.7.5-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.7.5-1
- Initial humble build
