# Meta Package
Name:           ros-humble-foonathan-memory-vendor
Version:        1.2.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-foonathan_memory_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-foonathan_memory_vendor
Requires:       ros2-humble-foonathan_memory_vendor-devel

Obsoletes: ros-humble-foonathan-memory-vendor < 1.2.0-1

%description
Foonathan/memory vendor package for Fast-RTPS.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.2.0-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.2.0-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.2.0-1
- Initial humble build
