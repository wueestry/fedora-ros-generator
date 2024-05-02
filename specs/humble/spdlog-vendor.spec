# Meta Package
Name:           ros-humble-spdlog-vendor
Version:        1.3.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            https://github.com/gabime/spdlog
Summary:        Meta package for ros2-humble-spdlog_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-spdlog_vendor
Requires:       ros2-humble-spdlog_vendor-devel

Obsoletes: ros-humble-spdlog-vendor < 1.3.1-1

%description
Wrapper around spdlog, providing nothing but a dependency on spdlog,
on some systems. On others, it provides an ExternalProject build of
spdlog.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.3.1-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.3.1-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.3.1-1
- Initial humble build
